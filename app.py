from agents.job_parser_agent import JobParserAgent
from core.services.ai_service import AIService
from core.utils.file_reader import read_text_file


def main():

    ai = AIService()

    parser = JobParserAgent(ai)

    job_text = read_text_file(
        "data/jobs/sample_job.txt"
    )

    job = parser.parse_job_description(
        job_text
    )

    print()

    print(job.model_dump_json(indent=4))


if __name__ == "__main__":
    main()