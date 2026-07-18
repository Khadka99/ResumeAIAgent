from core.builders.prompt_builder import PromptBuilder
from core.models.job_requirements import JobRequirements


def test_build_resume_prompt():

    job = JobRequirements(
        title="Accounting Clerk",
        company="Brandt",
        required_skills=[
            "Excel",
            "QuickBooks",
        ],
        responsibilities=[
            "Accounts Payable",
        ],
        qualifications=[
            "Diploma",
        ],
        summary="Accounting role.",
    )

    prompt = PromptBuilder.build_resume_prompt(
        master_resume="My Resume",
        job=job,
    )

    assert "Accounting Clerk" in prompt
    assert "Brandt" in prompt
    assert "QuickBooks" in prompt
