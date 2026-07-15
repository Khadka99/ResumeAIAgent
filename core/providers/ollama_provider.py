"""
Ollama implementation of the BaseLLM interface.
"""


from ollama import Client

client = Client(host="http://localhost:11434")

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
    Ollama implementation of BaseLLM.
    """

    def __init__(self) -> None:
        super().__init__(settings.OLLAMA_MODEL)

        self.client = Client(host="http://localhost:11434")

    @property
    def provider_name(self) -> str:
        return "Ollama"

    def ask(self, prompt: str) -> LLMResponse:
        """
        Send a prompt to the local Ollama model.
        """

        self.validate_prompt(prompt)
        self.log_request()

        try:

            response = self.client.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
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
                }
            )

        except LLMResponseError:
            raise

        except Exception as exc:

            logger.exception("Ollama request failed.")

            raise LLMProviderError(str(exc)) from exc