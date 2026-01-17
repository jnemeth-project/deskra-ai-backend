from typing import List, Dict, Tuple

from app.models.schemas import ChatAction
from app.core.llm import MockLLMClient


def decide_response(
    user_message: str,
    session_history: List[Dict[str, str]] | None = None
) -> Tuple[str, ChatAction, float]:
    """
    Core decision layer.
    - user_message: current user input
    - session_history: list of {role, content} dicts
    """

    if session_history is None:
        session_history = []

    llm = MockLLMClient()

    # Mock LLM response (offline, deterministic)
    response_text = llm.generate_response(
        user_message=user_message,
        history=session_history
    )

    # Very simple action logic for demo purposes
    if "password" in user_message.lower():
        action = ChatAction.escalate
        confidence = 0.6
    else:
        action = ChatAction.respond
        confidence = 0.9

    return response_text, action, confidence
