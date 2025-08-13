from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False
    created_at: datetime = datetime.now(timezone.utc)

class TaskCreate(TaskBase):
    pass

class TaskDB(TaskBase):
    id: str
    created_at: datetime = datetime.now(timezone.utc)

    class Config:
        orm_mode = True