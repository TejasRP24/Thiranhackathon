from pydantic import BaseModel
from typing import Optional

class ComplaintInput(BaseModel):
    description: str
    location: Optional[str] = None

class Task(BaseModel):
    issue: str
    department: str
    priority: str
    sla_hours: int
    status: str

class StatusUpdateRequest(BaseModel):
    new_status: str
    changed_by: str
    reason: str