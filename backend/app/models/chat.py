from datetime import datetime
from pydantic import BaseModel
from typing import List

class ChatMessage(BaseModel):
    content: str
    sender: str  # 'user' or 'bot'
    timestamp: datetime

class ChatHistory(BaseModel):
    user_id: str
    session_id: str
    messages: List[ChatMessage]
    started_at: datetime
    ended_at: datetime | None = None

    class Config:
        from_attributes = True
