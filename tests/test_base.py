import pytest

from core.models.llm_response import LLMResponse
from core.providers.base import BaseLLM


class DummyLLM(BaseLLM):

    @property
    def provider_name(self) -> str:
        return "Dummy"

    def ask(self, prompt: str) -> LLMResponse:
        return LLMResponse(
            content="Hello!",
            provider=self.provider_name,
            model=self.model,
        )


def test_dummy_provider():

    llm = DummyLLM(model="dummy-model")

    response = llm.ask("Hi")

    assert response.content == "Hello!"
    assert response.provider == "Dummy"
    assert response.model == "dummy-model"


def test_base_class_cannot_be_instantiated():

    with pytest.raises(TypeError):
        BaseLLM(model="test")