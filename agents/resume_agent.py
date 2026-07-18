"""
Agent responsible for customizing resumes.
"""

from core.builders.prompt_builder import PromptBuilder
from core.models.job_requirements import JobRequirements
from core.models.resume import Resume
from core.prompts.resume import RESUME_AGENT_SYSTEM_PROMPT
from core.services.ai_service import AIService
from core.utils.json_parser import parse_json


class ResumeAgent:
    """
    Generates a customized resume.
    """

    def __init__(self, ai_service: AIService):
        self.ai = ai_service

    def customize_resume(
        self,
        master_resume: str,
        job: JobRequirements,
    ) -> Resume:
        """
        Customize a resume for a target job.
        """

        prompt = PromptBuilder.build_resume_prompt(
            master_resume,
            job,
        )

        response = self.ai.ask(
            prompt=prompt,
            system_prompt=RESUME_AGENT_SYSTEM_PROMPT,
        )

        data = parse_json(response.content)

        return Resume.model_validate(data)
