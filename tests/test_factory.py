import pytest

from core.config import settings
from core.exceptions.llm_exceptions import UnsupportedProviderError
from core.factory import get_llm
from core.providers.ollama_provider import OllamaLLM
from core.providers.openai_provider import OpenAILLM


def test_get_openai(monkeypatch):

    monkeypatch.setattr(settings, "LLM_PROVIDER", "openai")

    llm = get_llm()

    assert isinstance(llm, OpenAILLM)


def test_get_ollama(monkeypatch):

    monkeypatch.setattr(settings, "LLM_PROVIDER", "ollama")

    llm = get_llm()

    assert isinstance(llm, OllamaLLM)


def test_invalid_provider(monkeypatch):

    monkeypatch.setattr(settings, "LLM_PROVIDER", "invalid")

    with pytest.raises(UnsupportedProviderError):
        get_llm()