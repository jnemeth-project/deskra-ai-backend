from fastapi import APIRouter

from app.models.schemas import ChatRequest, ChatResponse
from app.core.decision import decide_response
from app.core.memory import get_session_history, save_session_history

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/message", response_model=ChatResponse)
def handle_chat_message(payload: ChatRequest):
    # Load previous session messages (if any)
    session_history = get_session_history(payload.session_id)

    # Decide response
    response_text, action, confidence = decide_response(
        user_message=payload.message,
        session_history=session_history
    )

    # Save both user + assistant message to memory
    save_session_history(
        payload.session_id,
        user_message=payload.message,
        assistant_message=response_text
    )

    return ChatResponse(
        response=response_text,
        action=action,
        confidence=confidence
    )
