"""
AI Engineering Documentation Corpus Loader

This module provides utilities for loading the synthetic AI Engineering
documentation corpus used across multiple labs in the course.
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Optional


def get_corpus_path() -> Path:
    """Get the path to the corpus directory."""
    return Path(__file__).parent / "ai_engineering_docs"


def load_documents(doc_type: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Load documents from the corpus.
    
    Args:
        doc_type: Optional filter for document type. 
                  Options: 'api_reference', 'tutorial', 'concept', 
                           'troubleshooting', 'config'
                  If None, loads all documents.
    
    Returns:
        List of document dictionaries with keys:
        - id: Unique document identifier
        - type: Document type
        - title: Document title
        - category: Document category
        - content: Full document content (markdown)
        - tags: List of tags
    """
    corpus_path = get_corpus_path()
    all_docs = []
    
    # Map doc_type to file names
    type_to_file = {
        'api_reference': 'api_references.json',
        'tutorial': 'tutorials.json',
        'concept': 'concepts.json',
        'troubleshooting': 'troubleshooting.json',
        'config': 'config_files.json'
    }
    
    if doc_type:
        files_to_load = [type_to_file.get(doc_type)]
        if not files_to_load[0]:
            raise ValueError(f"Unknown doc_type: {doc_type}. Options: {list(type_to_file.keys())}")
    else:
        files_to_load = list(type_to_file.values())
    
    for filename in files_to_load:
        filepath = corpus_path / filename
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                docs = json.load(f)
                all_docs.extend(docs)
    
    return all_docs


def load_documents_as_text(doc_type: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Load documents and return them in a format suitable for RAG ingestion.
    
    Returns:
        List of dictionaries with:
        - text: The document content
        - metadata: Dictionary with id, type, title, category, tags
    """
    docs = load_documents(doc_type)
    
    return [
        {
            'text': doc['content'],
            'metadata': {
                'id': doc['id'],
                'type': doc['type'],
                'title': doc['title'],
                'category': doc.get('category', ''),
                'tags': doc.get('tags', [])
            }
        }
        for doc in docs
    ]


def get_corpus_stats() -> Dict[str, Any]:
    """Get statistics about the corpus."""
    docs = load_documents()
    
    stats = {
        'total_documents': len(docs),
        'by_type': {},
        'by_category': {},
        'total_characters': 0,
        'avg_document_length': 0
    }
    
    for doc in docs:
        # Count by type
        doc_type = doc['type']
        stats['by_type'][doc_type] = stats['by_type'].get(doc_type, 0) + 1
        
        # Count by category
        category = doc.get('category', 'Unknown')
        stats['by_category'][category] = stats['by_category'].get(category, 0) + 1
        
        # Count characters
        stats['total_characters'] += len(doc['content'])
    
    if docs:
        stats['avg_document_length'] = stats['total_characters'] // len(docs)
    
    return stats


def search_documents(query: str, doc_type: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Simple keyword search across documents.
    
    Args:
        query: Search query (case-insensitive)
        doc_type: Optional filter for document type
        
    Returns:
        List of matching documents
    """
    docs = load_documents(doc_type)
    query_lower = query.lower()
    
    matches = []
    for doc in docs:
        if (query_lower in doc['title'].lower() or 
            query_lower in doc['content'].lower() or
            any(query_lower in tag.lower() for tag in doc.get('tags', []))):
            matches.append(doc)
    
    return matches


# Sample documents for quick testing
SAMPLE_DOCS = [
    {
        'text': "The transformer architecture was introduced in the paper 'Attention Is All You Need' in 2017. It revolutionized natural language processing by replacing recurrent neural networks with self-attention mechanisms.",
        'metadata': {'source': 'sample', 'topic': 'transformers'}
    },
    {
        'text': "Retrieval-Augmented Generation (RAG) combines the power of large language models with external knowledge retrieval. This approach helps reduce hallucinations and provides up-to-date information.",
        'metadata': {'source': 'sample', 'topic': 'rag'}
    },
    {
        'text': "Prompt engineering is the practice of designing and optimizing prompts to get better results from language models. Techniques include few-shot learning, chain-of-thought prompting, and structured output formatting.",
        'metadata': {'source': 'sample', 'topic': 'prompt-engineering'}
    },
    {
        'text': "Vector databases are specialized databases optimized for storing and querying high-dimensional vectors. They use approximate nearest neighbor algorithms like HNSW for efficient similarity search.",
        'metadata': {'source': 'sample', 'topic': 'vector-db'}
    },
    {
        'text': "Temperature is a hyperparameter that controls the randomness of LLM outputs. Lower temperatures (0-0.3) produce more deterministic outputs, while higher temperatures (0.7-1.0) increase creativity and variation.",
        'metadata': {'source': 'sample', 'topic': 'llm-parameters'}
    }
]


if __name__ == "__main__":
    # Print corpus statistics
    stats = get_corpus_stats()
    print("AI Engineering Documentation Corpus")
    print("=" * 40)
    print(f"Total documents: {stats['total_documents']}")
    print(f"Total characters: {stats['total_characters']:,}")
    print(f"Average document length: {stats['avg_document_length']:,} chars")
    print("\nDocuments by type:")
    for doc_type, count in sorted(stats['by_type'].items()):
        print(f"  {doc_type}: {count}")
    print("\nDocuments by category:")
    for category, count in sorted(stats['by_category'].items()):
        print(f"  {category}: {count}")
