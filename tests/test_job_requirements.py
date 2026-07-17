from core.models.job_requirements import JobRequirements


def test_job_requirements_defaults():

    job = JobRequirements()

    assert job.title == ""

    assert job.company == ""

    assert job.required_skills == []

    assert job.preferred_skills == []

    assert job.summary == ""