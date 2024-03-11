from openai import OpenAI
import argparse
import os
from dotenv import load_dotenv

load_dotenv()

SYSTEM_MESSAGE = """
Answer the user with short, concise answers and code snippets.
Keep it to the point and don't go off-topic.
"""

def main():
    print("Starting GPT Shell Client")
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="*", type=str, help="Prompt for GPT-3 to complete")
    args = parser.parse_args()
    prompt = " ".join(args.prompt)
    print(f"Q: {prompt}")

    chat_history = []
    ask_gpt(prompt, chat_history, SYSTEM_MESSAGE)
    user_input = input(">_: ")
    while user_input != "":
        ask_gpt(user_input, chat_history, SYSTEM_MESSAGE)
        user_input = input(">_: ")
    print("Ending Session")

def ask_gpt(prompt: str, chat_history: list, system_message: str):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    user_prompt = {"role": "user", "content": prompt}
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        # response_format={ "type": "json_object" },
        messages=[
            {"role":"system", "content": system_message},
            *chat_history,
            user_prompt,
        ]
    )    
    content = response.choices[0].message.content
    chat_history.append(user_prompt)
    chat_history.append({ "role": "assistant", "content": content })
    content = content.strip()
    print("\n" + content)
    return content


if __name__ == '__main__':
    main()
