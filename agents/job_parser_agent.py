"""
Agent responsible for parsing job descriptions.
"""

from core.builders.prompt_builder import PromptBuilder
from core.models.job_requirements import JobRequirements
from core.prompts.job_parser import JOB_PARSER_SYSTEM_PROMPT
from core.services.ai_service import AIService
from core.utils.json_parser import parse_json

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
        """
        Parse a job description using the configured AI provider.
        """

        from core import PromptBuilder

        prompt = PromptBuilder.build_job_parser_prompt(
            job_description
        )

        response = self.ai.ask(
            prompt=prompt,
            system_prompt=JOB_PARSER_SYSTEM_PROMPT,
        )

        return self._build_job_requirements(response.content)

    def _build_job_requirements(
        self,
        json_text: str,
    ) -> JobRequirements:
        """
        Convert the JSON returned by the AI into a JobRequirements object.
        """

        data = parse_json(json_text)

        return JobRequirements.model_validate(data)