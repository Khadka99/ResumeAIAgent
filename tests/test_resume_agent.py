from agents.resume_agent import ResumeAgent
from core import JobRequirements
from core import LLMResponse
from core import BaseLLM
from core import AIService


class DummyLLM(BaseLLM):

    @property
    def provider_name(self):
        return "Dummy"

    def ask(self, prompt, system_prompt=None):
        return LLMResponse(
            content="""
{
    "professional_summary": "Accounting professional.",
    "skills": ["Excel", "QuickBooks"],
    "experience": ["Accounting Clerk at ABC Company"],
    "education": ["Diploma in Accounting"],
    "certifications": [],
    "projects": []
}
""",
            provider="Dummy",
            model="dummy",
        )


def test_resume_agent():

    service = AIService(DummyLLM("dummy"))

    agent = ResumeAgent(service)

    job = JobRequirements(title="Accounting Clerk")

    resume = agent.customize_resume(
        master_resume="My Resume",
        job=job,
    )

    assert resume.professional_summary == "Accounting professional."
    assert "Excel" in resume.skills