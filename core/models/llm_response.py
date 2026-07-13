"""
Standard response model returned by every LLM provider.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class LLMResponse:
    """
    Represents a standardized response from any Large Language Model.

    Every provider (OpenAI, Ollama, Gemini, etc.) should return this object.
    """

    content: str

    provider: str

    model: str

    input_tokens: int = 0

    output_tokens: int = 0

    latency: float = 0.0

    metadata: dict[str, Any] = field(default_factory=dict)

    def __str__(self) -> str:
        """Return only the generated content when printed."""
        return self.content