from typing import List, Dict


class MockLLMClient:
    """
    Offline mock LLM.
    No APIs, no external calls.
    Safe for demos.
    """

    def generate_response(
        self,
        user_message: str,
        history: List[Dict[str, str]] | None = None
    ) -> str:
        if history is None or len(history) == 0:
            return f"(Mock) I understand your question: '{user_message}'. How can I help further?"

        last_turns = history[-2:]
        context_summary = " | ".join(
            f"{m['role']}: {m['content']}" for m in last_turns
        )

        return (
            f"(Mock) Based on our previous messages ({context_summary}), "
            f"here is my response to: '{user_message}'."
        )
