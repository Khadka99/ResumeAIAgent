"""
Ollama implementation of the BaseLLM interface.
"""

from ollama import Client

from core.config import settings
from core.exceptions.llm_exceptions import (
    LLMProviderError,
    LLMResponseError,
)
from core.models.llm_response import LLMResponse
from core.providers.base import BaseLLM
from core.utils.logger import logger


class OllamaLLM(BaseLLM):
    """
    Ollama implementation of the BaseLLM interface.
    """

    def __init__(self) -> None:
        super().__init__(settings.OLLAMA_MODEL)

        # Create a client connected to the local Ollama server
        self.client = Client(host="http://localhost:11434")

    @property
    def provider_name(self) -> str:
        """
        Return the provider name.
        """
        return "Ollama"

    def ask(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> LLMResponse:
        """
        Send a prompt to the configured Ollama model.
        """

        self.validate_prompt(prompt)
        self.log_request()

        try:

            messages = []

            # Optional system prompt
            if system_prompt:
                messages.append(
                    {
                        "role": "system",
                        "content": system_prompt,
                    }
                )

            # User prompt
            messages.append(
                {
                    "role": "user",
                    "content": prompt,
                }
            )

            response = self.client.chat(
                model=self.model,
                messages=messages,
            )

            content = response.message.content.strip()

            if not content:
                raise LLMResponseError(
                    "Ollama returned an empty response."
                )

            return LLMResponse(
                content=content,
                provider=self.provider_name,
                model=self.model,
                metadata={
                    "done": getattr(response, "done", False),
                },
            )

        except LLMResponseError:
            raise

        except Exception as exc:
            logger.exception("Ollama request failed.")

            raise LLMProviderError(
                f"Ollama request failed: {exc}"
            ) from exc