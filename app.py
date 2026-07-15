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