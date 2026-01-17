class MockLLMClient:
    def generate(self, message: str) -> str:
        return (
            "This is a mock response from Deskra. "
            "LLM integration will be added later."
        )
