import json
import asyncio
from openai import OpenAI, AsyncOpenAI
from pydantic import BaseModel


class DocumentExtractor:
    """Single-document extractor using OpenAI with JSON mode and Pydantic validation."""

    def __init__(self, client: OpenAI, model: str = 'gpt-4o-mini'):
        self.client = client
        self.model = model

    def extract(self, document: str, schema: type[BaseModel]) -> BaseModel:
        schema_json = json.dumps(schema.model_json_schema(), indent=2)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    'role': 'system',
                    'content': f'Extract data according to this JSON schema:\n{schema_json}\nReturn only valid JSON. Use null for missing fields.',
                },
                {'role': 'user', 'content': f'Document:\n{document}'},
            ],
            response_format={'type': 'json_object'},
            temperature=0,
        )

        data = json.loads(response.choices[0].message.content)
        return schema(**data)


class BatchExtractor:
    """Batch document extractor with async support and concurrency control."""

    def __init__(self, client: OpenAI, model: str = 'gpt-4o-mini'):
        self.model = model
        self._sync_client = client

    async def _extract_one(
        self,
        async_client: AsyncOpenAI,
        document: str,
        schema: type[BaseModel],
        semaphore: asyncio.Semaphore,
    ) -> BaseModel:
        async with semaphore:
            schema_json = json.dumps(schema.model_json_schema(), indent=2)

            response = await async_client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        'role': 'system',
                        'content': f'Extract data according to this JSON schema:\n{schema_json}\nReturn only valid JSON. Use null for missing fields.',
                    },
                    {'role': 'user', 'content': f'Document:\n{document}'},
                ],
                response_format={'type': 'json_object'},
                temperature=0,
            )

            data = json.loads(response.choices[0].message.content)
            return schema(**data)

    async def extract_batch(
        self,
        documents: list[tuple[str, type[BaseModel]]],
        max_concurrent: int = 5,
    ) -> list[BaseModel | Exception]:
        async_client = AsyncOpenAI()
        semaphore = asyncio.Semaphore(max_concurrent)

        async def _safe(doc: str, schema: type[BaseModel]) -> BaseModel | Exception:
            try:
                return await self._extract_one(async_client, doc, schema, semaphore)
            except Exception as e:
                return e

        tasks = [_safe(doc, schema) for doc, schema in documents]
        return await asyncio.gather(*tasks)
