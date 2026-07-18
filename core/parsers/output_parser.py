"""
Utilities for parsing and normalizing LLM JSON responses.
"""

from typing import Any

from core.utils.json_parser import parse_json


LIST_FIELDS = {
    "required_skills",
    "preferred_skills",
    "responsibilities",
    "qualifications",
    "keywords",
    "skills",
    "experience",
    "education",
    "certifications",
    "projects",
}


def normalize_llm_output(data: dict[str, Any]) -> dict[str, Any]:
    """
    Normalize common LLM inconsistencies before validation.
    """

    for field in LIST_FIELDS:

        value = data.get(field)

        if value is None:
            data[field] = []

        elif isinstance(value, str):

            value = value.strip()

            if value == "":
                data[field] = []

            else:
                data[field] = [value]

    return data


def parse_and_normalize(json_text: str) -> dict[str, Any]:
    """
    Parse JSON and normalize values returned by an LLM.
    """

    data = parse_json(json_text)

    return normalize_llm_output(data)