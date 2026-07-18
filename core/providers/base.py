"""
Abstract base class for all LLM providers.
"""

from abc import ABC, abstractmethod

from core.exceptions.llm_exceptions import LLMResponseError
#from core.providers.ollama_provider import LLMResponse
from core.models.llm_response import LLMResponse
from core.utils.logger import logger


class BaseLLM(ABC):
    """
    Abstract base class that defines the interface
    every LLM provider must implement.
    """

    def __init__(self, model: str) -> None:
        self.model = model

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Return the provider name."""
        pass

    @abstractmethod
    def ask(
            self,
            prompt: str,
            system_prompt: str | None = None,
    ) -> LLMResponse:
        pass

    # ---------------------------------------------------------
    # Shared helper methods
    # ---------------------------------------------------------

    def validate_prompt(self, prompt: str) -> None:
        """
        Validate the user prompt.
        """

        if not prompt.strip():
            raise LLMResponseError("Prompt cannot be empty.")

    def log_request(self) -> None:
        """
        Log outgoing LLM request.
        """

        logger.info(
            "Sending request to %s (%s)",
            self.provider_name,
            self.model,
        )