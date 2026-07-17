"""
Agent responsible for parsing job descriptions.
"""

from core.models.job_requirements import JobRequirements
from core.prompts import JOB_PARSER_SYSTEM_PROMPT
from core.services.ai_service import AIService


class JobParserAgent:
    """
    Extracts structured information from job descriptions.
    """

    def __init__(self, ai_service: AIService) -> None:
        self.ai = ai_service

    def parse_job_description(
        self,
        job_description: str,
    ) -> JobRequirements:
        """
        Parse a job description.

        Implementation coming next.
        """

        raise NotImplementedError