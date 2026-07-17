"""
Structured representation of a parsed job description.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class JobRequirements:
    """
    Represents the important information extracted
    from a job description.
    """

    title: str = ""

    company: str = ""

    location: str = ""

    employment_type: str = ""

    experience: str = ""

    education: str = ""

    required_skills: list[str] = field(default_factory=list)

    preferred_skills: list[str] = field(default_factory=list)

    responsibilities: list[str] = field(default_factory=list)

    qualifications: list[str] = field(default_factory=list)

    keywords: list[str] = field(default_factory=list)

    summary: str = ""