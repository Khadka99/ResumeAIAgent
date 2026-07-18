"""
Pydantic model representing a customized resume.
"""

from pydantic import BaseModel, ConfigDict, Field


class Resume(BaseModel):
    """
    Structured representation of a customized resume.
    """

    model_config = ConfigDict(
        extra="ignore",
        str_strip_whitespace=True,
        validate_assignment=True,
    )

    professional_summary: str = ""

    skills: list[str] = Field(default_factory=list)

    experience: list[str] = Field(default_factory=list)

    education: list[str] = Field(default_factory=list)

    certifications: list[str] = Field(default_factory=list)

    projects: list[str] = Field(default_factory=list)
