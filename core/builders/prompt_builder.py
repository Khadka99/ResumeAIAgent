"""
Prompt Builder.

Responsible for creating prompts used by AI agents.
"""

from core import JobRequirements


class PromptBuilder:
    """
    Builds prompts for AI agents.
    """

    @staticmethod
    def build_job_parser_prompt(
        job_description: str,
    ) -> str:
        """
        Build the prompt used to parse
        a job description.
        """

        return job_description

    @staticmethod
    def build_resume_prompt(
            master_resume: str,
            job: JobRequirements,
    ) -> str:
        """
        Build the prompt for resume customization.
        """

        return f"""
    MASTER RESUME

    {master_resume}

    ==================================================

    TARGET JOB

    Title:
    {job.title}

    Company:
    {job.company}

    Location:
    {job.location}

    Experience:
    {job.experience}

    Education:
    {job.education}

    Required Skills:
    {", ".join(job.required_skills)}

    Preferred Skills:
    {", ".join(job.preferred_skills)}

    Responsibilities:
    {", ".join(job.responsibilities)}

    Qualifications:
    {", ".join(job.qualifications)}

    Keywords:
    {", ".join(job.keywords)}

    Summary:
    {job.summary}
    """