"""
Utilities for parsing JSON returned by LLMs.
"""

import json
import re

from core.exceptions.llm_exceptions import LLMResponseError


def parse_json(text: str) -> dict:
    """
    Parse JSON returned by an LLM.

    Handles:
    - Markdown code fences
    - Extra explanatory text
    - Plain JSON
    """

    if not text.strip():
        raise LLMResponseError("Empty response received from LLM.")

    # Remove markdown code fences
    cleaned = re.sub(
        r"```(?:json)?",
        "",
        text,
        flags=re.IGNORECASE,
    )

    cleaned = cleaned.replace("```", "").strip()

    # Extract first JSON object
    match = re.search(
        r"\{.*\}",
        cleaned,
        flags=re.DOTALL,
    )

    if match:
        cleaned = match.group(0)

    try:
        return json.loads(cleaned)

    except json.JSONDecodeError as exc:
        raise LLMResponseError(
            "LLM did not return valid JSON."
        ) from exc