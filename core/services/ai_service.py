"""
Central AI service used by all AI agents.

This service is responsible for communicating with the
configured LLM provider.
"""

from core.factory import get_llm
from core.models.llm_response import LLMResponse
from core.providers.base import BaseLLM
from core.utils.logger import logger


class AIService:
    """
    Central service responsible for interacting with
    the configured AI provider.
    """

    def __init__(self, llm: BaseLLM | None = None) -> None:
        """
        Initialize the AI service.

        If no provider is supplied,
        create one using the factory.
        """

        self.llm = llm or get_llm()

        logger.info(
            "AI Service initialized with %s (%s)",
            self.llm.provider_name,
            self.llm.model,
        )

    def ask(
            self,
            prompt: str,
            system_prompt: str | None = None,
    ) -> LLMResponse:
        return self.llm.ask(
            prompt=prompt,
            system_prompt=system_prompt,
        )