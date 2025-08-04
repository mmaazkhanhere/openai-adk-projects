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

class EmailWriterResponse(BaseModel):
    action: str = Field(..., description="Action taken by the agent")
    email_response: str = Field(..., description="Email response generated")