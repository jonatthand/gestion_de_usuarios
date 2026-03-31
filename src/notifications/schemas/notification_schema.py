from pydantic import BaseModel
from enum import Enum
from typing import Optional
from datetime import datetime

class ChannelEnum(str, Enum):
    email = "email"
    sms = "sms"
    push = "push"


class NotificationCreate(BaseModel):
    title: str
    message: str
    channel: ChannelEnum
    recipient: str

class NotificationUpdate(BaseModel):
    title: Optional[str] = None
    message: Optional[str] = None
    channel: Optional[str] = None
    recipient: Optional[str] = None

class NotificationResponse(BaseModel):
    id: int
    title: str
    message: str
    channel: str
    recipient: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True