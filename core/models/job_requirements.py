"""
Pydantic model representing a parsed job description.
"""

from pydantic import BaseModel, Field, ConfigDict


class JobRequirements(BaseModel):
    """
    Structured representation of a parsed job description.
    """

    model_config = ConfigDict(
        extra="ignore",
        str_strip_whitespace=True,
        validate_assignment=True,
    )

    title: str = ""

    company: str = ""

    location: str = ""

    employment_type: str = ""

    experience: str = ""

    education: str = ""

    required_skills: list[str] = Field(default_factory=list)

    preferred_skills: list[str] = Field(default_factory=list)

    responsibilities: list[str] = Field(default_factory=list)

    qualifications: list[str] = Field(default_factory=list)

    keywords: list[str] = Field(default_factory=list)

    summary: str = ""