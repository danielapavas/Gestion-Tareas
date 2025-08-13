from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False
    created_at: datetime = datetime.utcnow()
