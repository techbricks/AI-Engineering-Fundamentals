from pydantic import BaseModel, Field
from typing import Optional


class LineItem(BaseModel):
    description: str = Field(..., description="Item description")
    quantity: Optional[float] = Field(None, description="Quantity")
    unit_price: Optional[float] = Field(None, description="Price per unit")
    amount: float = Field(..., description="Line total")


class Invoice(BaseModel):
    invoice_number: str = Field(..., description="Invoice ID/number")
    invoice_date: str = Field(..., description="Date issued")
    due_date: Optional[str] = Field(None, description="Payment due date")
    vendor_name: str = Field(..., description="Company issuing invoice")
    customer_name: str = Field(..., description="Company being billed")
    line_items: list[LineItem] = Field(default_factory=list, description="List of items/services")
    subtotal: float = Field(..., description="Subtotal before tax")
    tax_amount: Optional[float] = Field(None, description="Tax amount")
    total: float = Field(..., description="Total amount due")
    payment_status: Optional[str] = Field(None, description="Payment status")


class ReceiptItem(BaseModel):
    description: str = Field(..., description="Item description")
    quantity: Optional[float] = Field(None, description="Quantity")
    price: float = Field(..., description="Item price")


class Receipt(BaseModel):
    receipt_number: str = Field(..., description="Receipt/transaction number")
    store_name: str = Field(..., description="Store or business name")
    date: Optional[str] = Field(None, description="Purchase date")
    items: list[ReceiptItem] = Field(default_factory=list, description="Purchased items")
    subtotal: Optional[float] = Field(None, description="Subtotal before tax")
    tax: Optional[float] = Field(None, description="Tax amount")
    total: float = Field(..., description="Total amount paid")
    payment_method: Optional[str] = Field(None, description="Payment method used")


class Experience(BaseModel):
    title: str = Field(..., description="Job title")
    company: str = Field(..., description="Company name")
    duration: Optional[str] = Field(None, description="Employment duration")
    description: Optional[str] = Field(None, description="Role description")


class Education(BaseModel):
    degree: str = Field(..., description="Degree or certification")
    institution: str = Field(..., description="School or university")
    year: Optional[str] = Field(None, description="Graduation year")


class Resume(BaseModel):
    full_name: str = Field(..., description="Candidate full name")
    email: Optional[str] = Field(None, description="Email address")
    phone: Optional[str] = Field(None, description="Phone number")
    location: Optional[str] = Field(None, description="City/region")
    summary: Optional[str] = Field(None, description="Professional summary")
    experience: list[Experience] = Field(default_factory=list, description="Work experience")
    education: list[Education] = Field(default_factory=list, description="Education history")
    skills: list[str] = Field(default_factory=list, description="Listed skills")


class Party(BaseModel):
    name: str = Field(..., description="Party name")
    role: Optional[str] = Field(None, description="Role in contract")


class Contract(BaseModel):
    contract_title: str = Field(..., description="Contract title")
    contract_type: str = Field(..., description="Type of contract")
    effective_date: Optional[str] = Field(None, description="Start/effective date")
    expiration_date: Optional[str] = Field(None, description="End/expiration date")
    parties: list[Party] = Field(default_factory=list, description="Parties involved")
    total_value: Optional[float] = Field(None, description="Contract monetary value")
    governing_law: Optional[str] = Field(None, description="Governing jurisdiction")


DOCUMENT_TYPES = ['invoice', 'receipt', 'resume', 'contract']

DOCUMENT_SCHEMAS: dict[str, type[BaseModel]] = {
    'invoice': Invoice,
    'receipt': Receipt,
    'resume': Resume,
    'contract': Contract,
}
