from core.llm import LLM


def main():

    print("=" * 50)
    print("Resume AI Agent")
    print("=" * 50)

    llm = LLM()

    question = input("\nAsk something:\n\n> ")

    answer = llm.ask(question)

    print("\n")
    print(answer)


if __name__ == "__main__":
    main()