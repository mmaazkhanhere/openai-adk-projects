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

class AgentResponse(BaseModel):
    category: Category = Field(..., description="Category of the email")
    summary: str = Field(..., description="Summary of the email")
    priority: Priority = Field(..., description="Priority of the email")
