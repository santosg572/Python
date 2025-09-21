import openai

# Load your OpenAI API key
openai.api_key = "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"


def generate_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Use the desired GPT model
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Usage example
if __name__ == "__main__":
    user_input = input("Ask ChatGPT: ")
    chatgpt_response = generate_chatgpt_response(user_input)
    print(f"ChatGPT says: {chatgpt_response}")

