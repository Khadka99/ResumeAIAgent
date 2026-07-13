from ollama import chat

response = chat(
    model="llama3.1:8b",
    messages=[
        {
            "role": "user",
            "content": "Say hello!"
        }
    ]
)

print(response["message"]["content"])