from pydantic import BaseModel
from typing import Literal

class NotificationCreateSchema(BaseModel):
    title: str
    content: str
    channel: Literal["email", "sms", "push"]