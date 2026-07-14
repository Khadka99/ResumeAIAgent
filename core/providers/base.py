"""
Abstract base class for all LLM providers.
"""

from abc import ABC, abstractmethod

from core.models.llm_response import LLMResponse


class BaseLLM(ABC):
    """
    Abstract base class that defines the interface
    every LLM provider must implement.
    """

    def __init__(self, model: str) -> None:
        """
        Initialize the provider.

        Args:
            model: Name of the language model.
        """
        self.model = model

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """
        Return the provider name.
        """
        pass

    @abstractmethod
    def ask(self, prompt: str) -> LLMResponse:
        """
        Send a prompt to the LLM.

        Args:
            prompt: User prompt.

        Returns:
            Standardized LLMResponse.
        """
        pass