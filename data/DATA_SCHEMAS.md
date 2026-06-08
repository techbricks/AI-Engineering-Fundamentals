# Document Data Schemas for Extraction Project

## Overview

Generate **5 examples of each document type** with varying formats and styles. Each document should be a realistic text file that looks like it came from different sources.

---

## Document Type 1: INVOICES

### Fields to Extract

```python
class Invoice(BaseModel):
    invoice_number: str           # e.g., "INV-2024-001", "A-12345"
    invoice_date: str             # e.g., "2024-01-15", "January 15, 2024"
    due_date: Optional[str]       # e.g., "2024-02-15", "Net 30"
    
    vendor_name: str              # Company issuing the invoice
    vendor_address: Optional[str] # Full address or partial
    vendor_email: Optional[str]   # Contact email
    vendor_phone: Optional[str]   # Contact phone
    
    customer_name: str            # Company/person being billed
    customer_address: Optional[str]
    
    line_items: list[LineItem]    # List of products/services
    
    subtotal: float               # Sum before tax
    tax_rate: Optional[float]     # e.g., 0.08 for 8%
    tax_amount: Optional[float]   # Dollar amount of tax
    discount: Optional[float]     # Any discount applied
    total: float                  # Final amount due
    
    payment_method: Optional[str] # e.g., "Credit Card", "Bank Transfer"
    payment_status: Optional[str] # e.g., "Paid", "Pending", "Overdue"
    notes: Optional[str]          # Additional notes

class LineItem(BaseModel):
    description: str              # Product/service name
    quantity: Optional[float]     # Number of units
    unit_price: Optional[float]   # Price per unit
    amount: float                 # Line total
```

### Variation Guidelines for 5 Invoices

| File Name | Style | Format Quirks |
|-----------|-------|---------------|
| `invoice_001_corporate.txt` | Formal corporate | Full headers, all fields present, USD |
| `invoice_002_simple_receipt.txt` | ✅ Already exists | Receipt style, minimal fields |
| `invoice_003_email_style.txt` | ✅ Already exists | Embedded in email text |
| `invoice_004_european_format.txt` | ✅ Already exists | European date format, EUR |
| `invoice_005_handwritten_style.txt` | ✅ Already exists | Casual, abbreviated |
| `invoice_006_minimal.txt` | ✅ Already exists | Single paragraph, minimal |

**You only need to create:** `invoice_001_corporate.txt` (formal with all fields)

---

## Document Type 2: RECEIPTS

### Fields to Extract

```python
class Receipt(BaseModel):
    receipt_number: str           # e.g., "REC-001", "TXN-12345"
    receipt_date: str             # Date of purchase
    receipt_time: Optional[str]   # Time of purchase if available
    
    store_name: str               # Business name
    store_address: Optional[str]  # Location
    store_phone: Optional[str]    # Contact
    
    items: list[ReceiptItem]      # Purchased items
    
    subtotal: float               # Before tax
    tax: Optional[float]          # Tax amount
    total: float                  # Final amount
    
    payment_method: str           # Cash, Credit, Debit, etc.
    card_last_four: Optional[str] # Last 4 digits if card payment
    
    cashier: Optional[str]        # Cashier name/ID
    register_number: Optional[str] # Register/terminal ID

class ReceiptItem(BaseModel):
    name: str                     # Item name
    quantity: Optional[int]       # Number purchased
    price: float                  # Item price
    sku: Optional[str]            # Product code if shown
```

### Variation Guidelines for 5 Receipts

| File Name | Style | Format Quirks |
|-----------|-------|---------------|
| `receipt_001_retail.txt` | Retail store | Long itemized list, SKUs, loyalty points |
| `receipt_002_restaurant.txt` | Restaurant | Tips, server name, table number |
| `receipt_003_grocery.txt` | Grocery store | Many items, weight-based items, coupons |
| `receipt_004_gas_station.txt` | Gas station | Fuel purchase, pump number, gallons |
| `receipt_005_online.txt` | E-commerce | Order number, shipping info, digital format |

---

## Document Type 3: RESUMES

### Fields to Extract

```python
class Resume(BaseModel):
    # Personal Information
    full_name: str                # Candidate name
    email: str                    # Contact email
    phone: Optional[str]          # Contact phone
    location: Optional[str]       # City, State or full address
    linkedin: Optional[str]       # LinkedIn URL
    github: Optional[str]         # GitHub URL
    portfolio: Optional[str]      # Personal website
    
    # Professional Summary
    summary: Optional[str]        # Brief professional summary
    
    # Work Experience
    experience: list[WorkExperience]
    
    # Education
    education: list[Education]
    
    # Skills
    skills: list[str]             # List of skills
    
    # Certifications
    certifications: Optional[list[str]]
    
    # Languages
    languages: Optional[list[str]]
    
    # Total years of experience (calculated or stated)
    years_of_experience: Optional[int]

class WorkExperience(BaseModel):
    company: str                  # Company name
    title: str                    # Job title
    location: Optional[str]       # Work location
    start_date: str               # Start date
    end_date: Optional[str]       # End date or "Present"
    is_current: bool              # True if current job
    responsibilities: list[str]   # Bullet points of duties
    achievements: Optional[list[str]]  # Quantified achievements

class Education(BaseModel):
    institution: str              # School/University name
    degree: str                   # Degree type (BS, MS, PhD, etc.)
    field_of_study: str           # Major/Field
    graduation_date: Optional[str] # Graduation year/date
    gpa: Optional[float]          # GPA if listed
    honors: Optional[str]         # Cum laude, Dean's list, etc.
```

### Variation Guidelines for 5 Resumes

| File Name | Style | Format Quirks |
|-----------|-------|---------------|
| `resume_001_software_engineer.txt` | Tech professional | GitHub, technical skills, multiple jobs |
| `resume_002_recent_graduate.txt` | Entry-level | Education-focused, internships, projects |
| `resume_003_executive.txt` | Senior executive | Long career, board positions, achievements |
| `resume_004_career_changer.txt` | Transitioning careers | Mixed industries, transferable skills |
| `resume_005_freelancer.txt` | Freelance/Consultant | Project-based, multiple clients |

---

## Document Type 4: CONTRACTS

### Fields to Extract

```python
class Contract(BaseModel):
    # Document Identification
    contract_number: Optional[str] # Contract ID/reference
    contract_title: str           # Name/type of contract
    contract_type: str            # Employment, Service, NDA, Lease, etc.
    
    # Dates
    effective_date: str           # When contract starts
    expiration_date: Optional[str] # When contract ends
    execution_date: Optional[str]  # When signed
    
    # Parties
    parties: list[ContractParty]  # All parties involved
    
    # Financial Terms
    total_value: Optional[float]  # Total contract value
    payment_terms: Optional[str]  # Payment schedule/terms
    currency: Optional[str]       # USD, EUR, etc.
    
    # Key Terms
    termination_notice_days: Optional[int]  # Days notice for termination
    renewal_terms: Optional[str]  # Auto-renewal, manual, etc.
    governing_law: Optional[str]  # Jurisdiction (e.g., "State of California")
    
    # Confidentiality
    has_confidentiality_clause: bool
    has_non_compete: bool
    non_compete_duration: Optional[str]
    
    # Deliverables (for service contracts)
    deliverables: Optional[list[str]]
    
    # Signatures
    signatures: list[Signature]

class ContractParty(BaseModel):
    party_type: str               # "First Party", "Second Party", "Contractor", "Client"
    name: str                     # Legal name
    role: str                     # Their role in contract
    address: Optional[str]        # Legal address
    representative: Optional[str] # Person signing on behalf

class Signature(BaseModel):
    party_name: str               # Who signed
    signer_name: Optional[str]    # Name of person
    signer_title: Optional[str]   # Title of signer
    date_signed: Optional[str]    # Signature date
    is_signed: bool               # Whether signature is present
```

### Variation Guidelines for 5 Contracts

| File Name | Style | Format Quirks |
|-----------|-------|---------------|
| `contract_001_employment.txt` | Employment agreement | Salary, benefits, termination, non-compete |
| `contract_002_service.txt` | Service/consulting agreement | SOW, deliverables, milestones |
| `contract_003_nda.txt` | Non-disclosure agreement | Confidentiality terms, duration |
| `contract_004_lease.txt` | Office/equipment lease | Monthly payments, term, conditions |
| `contract_005_freelance.txt` | Freelance/independent contractor | Project scope, IP rights, payment |

---

## File Naming Convention

```
output/labs/module-03-prompt-engineering/data/
├── invoices/
│   ├── invoice_001_corporate.txt
│   ├── invoice_002_simple_receipt.txt  (move existing)
│   ├── invoice_003_email_style.txt     (move existing)
│   ├── invoice_004_european_format.txt (move existing)
│   ├── invoice_005_handwritten_style.txt (move existing)
│   └── invoice_006_minimal.txt         (move existing)
├── receipts/
│   ├── receipt_001_retail.txt
│   ├── receipt_002_restaurant.txt
│   ├── receipt_003_grocery.txt
│   ├── receipt_004_gas_station.txt
│   └── receipt_005_online.txt
├── resumes/
│   ├── resume_001_software_engineer.txt
│   ├── resume_002_recent_graduate.txt
│   ├── resume_003_executive.txt
│   ├── resume_004_career_changer.txt
│   └── resume_005_freelancer.txt
└── contracts/
    ├── contract_001_employment.txt
    ├── contract_002_service.txt
    ├── contract_003_nda.txt
    ├── contract_004_lease.txt
    └── contract_005_freelance.txt
```

---

## Data Generation Prompt Template

Use this prompt with a cheaper/faster model to generate each document:

```
Generate a realistic {document_type} document in plain text format.

Requirements:
- Document style: {style_description}
- Format quirks: {format_quirks}
- Make it look like a real document, not a template
- Include realistic company names, addresses, dates
- Use realistic dollar amounts and quantities
- Vary the formatting (some structured, some free-form)
- Include some optional fields, omit others naturally

The document should be extractable for these fields:
{list_of_fields}

Generate ONLY the document text, no explanations.
```

---

## Summary: What to Generate

| Type | Files Needed | Already Exist |
|------|--------------|---------------|
| Invoices | 1 new | 5 existing |
| Receipts | 5 new | 0 |
| Resumes | 5 new | 0 |
| Contracts | 5 new | 0 |
| **TOTAL** | **16 new files** | **5 existing** |

---

## Example Ground Truth JSON (for evaluation)

For each document, also generate a corresponding JSON ground truth file:

```
data/
├── invoices/
│   ├── invoice_001_corporate.txt
│   └── invoice_001_corporate.json  # Ground truth extraction
```

This allows automated evaluation of extraction accuracy.
