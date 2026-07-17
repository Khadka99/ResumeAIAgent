# """
# Resume AI Agent - CLI entry point.
#
# Two modes:
#   1. Chat        - talk directly to the configured LLM (original behavior)
#   2. Run Pipeline - paste a job description + resume, get back a tailored
#                     resume, a cover letter, and an ATS match report
#
# Outputs from a pipeline run are saved to outputs/<timestamp>/ so nothing
# is lost when the terminal window closes.
# """
#
# import sys
# from datetime import datetime
# from pathlib import Path
#
# from agents.orchestrator import ResumeOrchestrator
# from core.exceptions.agent_exceptions import AgentError
# from core.services.ai_service import AIService
#
# OUTPUT_DIR = Path("outputs")
#
#
# def flush_input_buffer() -> None:
#     """
#     Discard any characters already sitting in the terminal's input queue.
#
#     Windows consoles dump an entire clipboard paste into the input queue
#     at once, regardless of which prompt is currently active. If a paste
#     contains more than the current prompt expects (e.g. a resume paste
#     that accidentally also includes a cover letter draft after the END
#     marker), the leftover lines would otherwise silently answer the next
#     prompt(s) instead of being ignored. Call this right after any
#     multi-line paste to discard whatever's left over before the next
#     prompt appears.
#     """
#     try:
#         import msvcrt  # Windows only
#         while msvcrt.kbhit():
#             msvcrt.getch()
#     except ImportError:
#         try:
#             import termios
#             termios.tcflush(sys.stdin, termios.TCIFLUSH)
#         except Exception:
#             pass  # best-effort only — not fatal if this isn't supported
#
#
# def read_multiline(prompt: str) -> str:
#     """
#     Collect multi-line pasted text from the terminal.
#
#     Paste your text, then type END on its own line and hit Enter.
#     """
#     print(prompt)
#     print("(paste your text, then type END on its own line to finish)")
#     lines = []
#     while True:
#         line = input()
#         if line.strip() == "END":
#             break
#         lines.append(line)
#     return "\n".join(lines)
#
#
# def run_chat(ai: AIService) -> None:
#     """Original simple chat loop."""
#     print(f"\nProvider : {ai.llm.provider_name}")
#     print(f"Model    : {ai.llm.model}")
#     print("(type 'quit' or 'exit' to return to the menu)")
#
#     while True:
#         prompt = input("\nYou > ")
#         if prompt.lower() in {"quit", "exit"}:
#             break
#         response = ai.ask(prompt)
#         print(f"\nAI > {response.content}")
#
#
# def run_pipeline(ai: AIService) -> None:
#     """Paste a job description + resume, get tailored outputs back."""
#     job_text = read_multiline("\nPaste the job description:")
#     flush_input_buffer()
#     if not job_text.strip():
#         print("No job description provided — returning to menu.")
#         return
#
#     resume_text = read_multiline("\nPaste your current resume:")
#     flush_input_buffer()
#     if not resume_text.strip():
#         print("No resume provided — returning to menu.")
#         return
#
#     tone = input("\nCover letter tone [professional]: ").strip() or "professional"
#     flush_input_buffer()
#
#     orchestrator = ResumeOrchestrator(ai)
#
#     print("\nRunning pipeline (parsing job -> tailoring resume -> cover letter -> ATS score)...")
#     try:
#         result = orchestrator.run(job_text, resume_text, tone=tone)
#     except AgentError as exc:
#         print(f"\nPipeline failed: {exc}")
#         return
#
#     print("\n" + "=" * 60)
#     print(f"Job          : {result.job.title} @ {result.job.company or 'N/A'}")
#     print(f"ATS Score    : {result.ats_report.match_score}/100")
#     print(f"Missing kw   : {', '.join(result.ats_report.missing_keywords) or 'none'}")
#     print("=" * 60)
#
#     run_dir = OUTPUT_DIR / datetime.now().strftime("%Y%m%d_%H%M%S")
#     run_dir.mkdir(parents=True, exist_ok=True)
#
#     formatting_issues_lines = (
#         [f"- {i}" for i in result.ats_report.formatting_issues]
#         or ["- none found"]
#     )
#
#     (run_dir / "tailored_resume.md").write_text(result.tailored_resume, encoding="utf-8")
#     (run_dir / "cover_letter.txt").write_text(result.cover_letter, encoding="utf-8")
#     (run_dir / "ats_report.md").write_text(
#         "\n".join(
#             [
#                 f"# ATS Report — {result.job.title}",
#                 "",
#                 f"**Match score:** {result.ats_report.match_score}/100",
#                 "",
#                 f"**Summary:** {result.ats_report.summary}",
#                 "",
#                 "## Matched keywords",
#                 *[f"- {k}" for k in result.ats_report.matched_keywords],
#                 "",
#                 "## Missing keywords",
#                 *[f"- {k}" for k in result.ats_report.missing_keywords],
#                 "",
#                 "## Formatting issues",
#                 *formatting_issues_lines,
#                 "",
#                 "## Recommendations",
#                 *[f"- {r}" for r in result.ats_report.recommendations],
#             ]
#         ),
#         encoding="utf-8",
#     )
#
#     print(f"\nSaved to {run_dir}/")
#     print("  - tailored_resume.md")
#     print("  - cover_letter.txt")
#     print("  - ats_report.md")
#
#
# def main() -> None:
#     print("=" * 60)
#     print("Resume AI Agent")
#     print("=" * 60)
#
#     ai = AIService()
#     print(f"\nProvider : {ai.llm.provider_name}")
#     print(f"Model    : {ai.llm.model}")
#
#     while True:
#         print("\nWhat would you like to do?")
#         print("  1) Chat with the AI")
#         print("  2) Run the resume pipeline (job -> tailored resume + cover letter + ATS score)")
#         print("  3) Quit")
#         choice = input("> ").strip()
#
#         if choice == "1":
#             run_chat(ai)
#         elif choice == "2":
#             run_pipeline(ai)
#         elif choice in {"3", "quit", "exit"}:
#             print("\nGoodbye!")
#             break
#         else:
#             print("Please enter 1, 2, or 3.")
#
#
# if __name__ == "__main__":
#     main()



from core.services.ai_service import AIService

def main():

    print("=" * 60)
    print("Resume AI Agent")
    print("=" * 60)

    ai = AIService()

    print(f"\nProvider : {ai.llm.provider_name}")
    print(f"Model    : {ai.llm.model}")

    while True:

        prompt = input("\nYou > ")

        if prompt.lower() in {"quit", "exit"}:
            print("\nGoodbye!")
            break

        response = ai.ask(prompt)

        print(f"\nAI > {response.content}")


if __name__ == "__main__":
    main()
