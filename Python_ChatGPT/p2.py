import openai

# Load your OpenAI API key
#openai.api_key = 


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

