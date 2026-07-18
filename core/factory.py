"""
Factory for creating LLM providers.
"""

from core import settings
from core import UnsupportedProviderError
from core import BaseLLM
from core import OllamaLLM
from core import OpenAILLM
from core import logger


def get_llm() -> BaseLLM:
    """
    Create and return the configured LLM provider.
    """

    provider = settings.LLM_PROVIDER.lower()

    logger.info("Loading LLM provider: %s", provider)

    if provider == "openai":
        return OpenAILLM()

    if provider == "ollama":
        return OllamaLLM()

    raise UnsupportedProviderError(
        f"Unsupported LLM provider: {provider}"
    )