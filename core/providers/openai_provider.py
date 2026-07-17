"""
OpenAI implementation of the BaseLLM interface.
"""

from openai import OpenAI

from core.config import settings
from core.exceptions.llm_exceptions import (
    LLMProviderError,
    LLMResponseError,
)
from core.models.llm_response import LLMResponse
from core.providers.base import BaseLLM
from core.utils.logger import logger
from core.utils.retry import retry_api


class OpenAILLM(BaseLLM):
    """
    OpenAI implementation of BaseLLM.
    """

    def __init__(self) -> None:
        super().__init__(settings.OPENAI_MODEL)

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    @property
    def provider_name(self) -> str:
        return "OpenAI"

    @retry_api
    def ask(
            self,
            prompt: str,
            system_prompt: str | None = None,
    ) -> LLMResponse:
        """
        Send a prompt to OpenAI.
        """

        self.validate_prompt(prompt)
        self.log_request()

        try:

            response = self.client.responses.create(
                model=self.model,
                input=prompt,
            )

            content = response.output_text.strip()

            if not content:
                raise LLMResponseError(
                    "OpenAI returned an empty response."
                )

            usage = getattr(response, "usage", None)

            return LLMResponse(
                content=content,
                provider=self.provider_name,
                model=self.model,
                input_tokens=usage.input_tokens if usage else 0,
                output_tokens=usage.output_tokens if usage else 0,
            )


        except LLMResponseError:

            raise


        except Exception as exc:

            logger.exception("OpenAI request failed.")

            raise LLMProviderError(str(exc)) from exc