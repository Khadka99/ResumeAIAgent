"""
Factory for creating LLM providers.
"""

from core.config import settings
from core.exceptions.llm_exceptions import UnsupportedProviderError
from core.providers.base import BaseLLM
from core.providers.ollama_provider import OllamaLLM
from core.providers.openai_provider import OpenAILLM
from core.utils.logger import logger


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