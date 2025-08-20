from pydantic import BaseModel, EmailStr
from datetime import datetime

class JobCreate(BaseModel):
    tweet_id: str | None = None
    title: str | None = None
    company: str | None = None
    location: str | None = None
    url: str | None = None
    raw_text: str

class JobOut(JobCreate):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class SubscribeIn(BaseModel):
    email: EmailStr
    prefs: str | None = None

class SubscribeOut(BaseModel):
    id: int
    email: EmailStr
    prefs: str | None
    subscribed_at: datetime
    class Config:
        from_attributes = True
