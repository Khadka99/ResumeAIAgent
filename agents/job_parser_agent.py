# """
# Agent responsible for parsing job descriptions.
# """
#
# from core.builders.prompt_builder import PromptBuilder
# from core.models.job_requirements import JobRequirements
# from core.prompts.job_parser import JOB_PARSER_SYSTEM_PROMPT
# from core.services.ai_service import AIService
# from core.utils.json_parser import parse_json
#
# class JobParserAgent:
#     """
#     Parses job descriptions into structured JobRequirements.
#     """
#
#     def __init__(self, ai_service: AIService):
#         self.ai = ai_service
#
#     def parse_job_description(
#         self,
#         job_description: str,
#     ) -> JobRequirements:
#         """
#         Parse a job description using the configured AI provider.
#         """
#
#         from core.builders.prompt_builder import PromptBuilder
#
#         prompt = PromptBuilder.build_job_parser_prompt(
#             job_description
#         )
#
#         response = self.ai.ask(
#             prompt=prompt,
#             system_prompt=JOB_PARSER_SYSTEM_PROMPT,
#         )
#         print("\n========== RAW LLM RESPONSE ==========\n")
#         print(response.content)
#         print("\n======================================\n")
#         return self._build_job_requirements(response.content)
#
#     def _build_job_requirements(
#         self,
#         json_text: str,
#     ) -> JobRequirements:
#         """
#         Convert the JSON returned by the AI into a JobRequirements object.
#         """
#
#         data = parse_json(json_text)
#
#         return JobRequirements.model_validate(data)




#New code#

"""
Agent responsible for parsing job descriptions.
"""

from core.builders.prompt_builder import PromptBuilder
from core.models.job_requirements import JobRequirements
from core.prompts.job_parser import JOB_PARSER_SYSTEM_PROMPT
from core.services.ai_service import AIService
"""from core.utils.json_parser import parse_json"""
from core.parsers.output_parser import parse_and_normalize


class JobParserAgent:
    """
    Parses job descriptions into structured JobRequirements.
    """

    def __init__(self, ai_service: AIService):
        self.ai = ai_service

    def parse_job_description(
        self,
        job_description: str,
        max_retries: int = 2,
    ) -> JobRequirements:
        """
        Parse a job description using the configured AI provider.
        Retries automatically if JSON is invalid.
        """

        prompt = PromptBuilder.build_job_parser_prompt(job_description)

        for attempt in range(max_retries + 1):
            response = self.ai.ask(
                prompt=prompt,
                system_prompt=JOB_PARSER_SYSTEM_PROMPT,
            )

            raw = response.content
            print("\n========== RAW LLM RESPONSE ==========\n")
            print(raw)
            print("\n======================================\n")

            try:
                return self._build_job_requirements(raw)
            except Exception as e:
                print(f"[WARN] JSON parsing failed (attempt {attempt + 1}/{max_retries + 1}): {e}")

                if attempt < max_retries:
                    # Force the model to re‑output strict JSON
                    prompt = (
                        f"{prompt}\n\n"
                        "The previous output was not valid JSON. "
                        "Return ONLY valid JSON. No markdown. No commentary."
                    )
                else:
                    raise ValueError(
                        f"Failed to parse job description after {max_retries + 1} attempts.\n"
                        f"Last raw output:\n{raw}"
                    )

    def _clean_json_text(self, text: str) -> str:
        """
        Remove markdown fences and surrounding noise.
        """

        # Strip markdown ```json fences
        if "```" in text:
            text = text.replace("```json", "").replace("```", "").strip()

        # Remove accidental leading/trailing text
        # Heuristic: JSON must start with { or [
        start = min(
            (i for i, ch in enumerate(text) if ch in "{["),
            default=0
        )
        end = max(
            (i for i, ch in enumerate(text) if ch in "}]"),
            default=len(text)
        ) + 1

        return text[start:end]

    def _build_job_requirements(self, json_text: str) -> JobRequirements:
        """
        Build a validated JobRequirements model from LLM output.
        """

        data = parse_and_normalize(json_text)

        return JobRequirements.model_validate(data)
