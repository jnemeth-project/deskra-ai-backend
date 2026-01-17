from pydantic import BaseModel, Field
from typing import Optional, Dict
from enum import Enum


class Channel(str, Enum):
    web = "web"
    widget = "widget"
    jira = "jira"
    zendesk = "zendesk"


class ChatRequest(BaseModel):
    session_id: str = Field(..., description="Client session identifier")
    message: str = Field(..., description="User message")
    channel: Channel = Field(..., description="Source channel")
    metadata: Optional[Dict] = None


class ChatAction(str, Enum):
    respond = "respond"
    clarify = "clarify"
    escalate = "escalate"


class ChatResponse(BaseModel):
    response: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    action: ChatAction
