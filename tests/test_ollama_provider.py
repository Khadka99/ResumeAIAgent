from core.models.llm_response import LLMResponse
from core.providers.ollama_provider import OllamaLLM


def test_provider_name():

    llm = OllamaLLM()

    assert llm.provider_name == "Ollama"


def test_model():

    llm = OllamaLLM()

    assert llm.model != ""


def test_real_request():

    llm = OllamaLLM()

    response = llm.ask(
        "What is the capital of Canada?"
    )

    assert isinstance(response, LLMResponse)

    assert "Ottawa" in response.content