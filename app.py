from core.factory import get_llm


def main():

    print("=" * 60)
    print("Resume AI Agent")
    print("=" * 60)

    llm = get_llm()

    print(f"\nProvider : {llm.provider_name}")
    print(f"Model    : {llm.model}")

    while True:

        prompt = input("\nYou > ")

        if prompt.lower() in {"exit", "quit"}:
            print("\nGoodbye!")
            break

        response = llm.ask(prompt)

        print(f"\nAI > {response.content}")


if __name__ == "__main__":
    main()