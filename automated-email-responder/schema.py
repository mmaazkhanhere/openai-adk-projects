from enum import Enum
from pydantic import BaseModel, Field

class Category(Enum):
    URGENT = "urgent"
    SUPPORT_REQUEST = "support_request"
    SALES_LEAD = "sales_lead"
    GENERAL_INQUIRY = "general_inquiry"
    SPAM = "spam"

class Priority(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class EmailCategory(BaseModel):
    category: Category = Field(..., description="Category of the email")
    reason: str = Field(..., description="Reason for the category")

class CategorizationResponse(BaseModel):
    category: Category  # The classification of the email: Urgent, Support Request, General Inquiry, Sales Lead, or Spam
    summary: str | None = None  # Brief summary of the email content (for Urgent/Support Request)
    priority: None| str = None  # Priority level: High, Medium, or Low (for Urgent/Support Request)
    query: None| str = None  # Extracted query/question (for General Inquiry)
    company: None| str = None  # Company name (for Sales Lead, default "Unknown")
    contact_person: None| str = None  # Contact person/email (for Sales Lead, default "Unknown")
    product_interest: None| str = None

class EmailWriterResponse(BaseModel):
    action: str = Field(..., description="Action taken by the agent")
    email_response: str = Field(..., description="Email response generated")