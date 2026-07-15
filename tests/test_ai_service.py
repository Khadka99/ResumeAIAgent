from core.models.llm_response import LLMResponse
from core.providers.base import BaseLLM
from core.services.ai_service import AIService


class DummyLLM(BaseLLM):

    @property
    def provider_name(self) -> str:
        return "Dummy"

    def ask(self, prompt: str) -> LLMResponse:

        return LLMResponse(
            content="Hello World",
            provider="Dummy",
            model=self.model,
        )


def test_ai_service():

    llm = DummyLLM("dummy")

    service = AIService(llm)

    response = service.ask("Hi")

    assert response.content == "Hello World"

    assert response.provider == "Dummy"

    assert response.model == "dummy"

