"""Shared test fixtures for agent tests."""
from core import LLMResponse
from core import BaseLLM


class DummyLLM(BaseLLM):
    """
    A fake LLM provider that returns a fixed response, so agent tests
    exercise real parsing/validation logic without hitting a real API.
    """

    def __init__(self, content: str, model: str = "dummy-model") -> None:
        super().__init__(model)
        self._content = content

    @property
    def provider_name(self) -> str:
        return "Dummy"

    def ask(self, prompt: str) -> LLMResponse:
        return LLMResponse(content=self._content, provider="Dummy", model=self.model)


class SequencedDummyLLM(BaseLLM):
    """
    A fake LLM that returns a different canned response on each successive
    call, in order. Used for orchestrator tests where each agent in the
    pipeline expects a different kind of response from the same LLM call.
    """

    def __init__(self, responses: list[str], model: str = "dummy-model") -> None:
        super().__init__(model)
        self._responses = list(responses)
        self._calls = 0

    @property
    def provider_name(self) -> str:
        return "Dummy"

    def ask(self, prompt: str) -> LLMResponse:
        content = self._responses[self._calls]
        self._calls += 1
        return LLMResponse(content=content, provider="Dummy", model=self.model)
