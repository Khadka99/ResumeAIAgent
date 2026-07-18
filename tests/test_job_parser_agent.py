"""
Agent responsible for parsing job descriptions.
"""

from core import JobRequirements
from core import JOB_PARSER_SYSTEM_PROMPT
from core import AIService
from core import parse_json


class JobParserAgent:
    """
    Parses job descriptions into structured JobRequirements.
    """

    def __init__(self, ai_service: AIService):
        self.ai = ai_service

    def parse_job_description(
        self,
        job_description: str,
    ) -> JobRequirements:

        response = self.ai.ask(
            prompt=job_description,
            system_prompt=JOB_PARSER_SYSTEM_PROMPT,
        )

        return self._build_job_requirements(
            response.content
        )

    def _build_job_requirements(
        self,
        json_text: str,
    ) -> JobRequirements:

        data = parse_json(json_text)

        return JobRequirements.model_validate(data)