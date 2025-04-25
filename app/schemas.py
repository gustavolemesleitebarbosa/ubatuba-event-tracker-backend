from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class EventBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    date: datetime
    location: str = Field(..., min_length=1, max_length=100)

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    date: Optional[datetime] = None
    location: Optional[str] = Field(None, min_length=1, max_length=100)

class Event(EventBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True 