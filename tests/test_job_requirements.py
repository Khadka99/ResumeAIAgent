from core import JobRequirements


def test_defaults():

    job = JobRequirements()

    assert job.title == ""

    assert job.company == ""

    assert job.required_skills == []

    assert job.summary == ""


def test_validation():

    job = JobRequirements.model_validate(
        {
            "title": "Accounting Clerk",
            "required_skills": [
                "Excel",
                "QuickBooks",
            ],
        }
    )

    assert job.title == "Accounting Clerk"

    assert "Excel" in job.required_skills