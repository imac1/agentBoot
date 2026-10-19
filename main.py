
import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError(
        "OPENROUTER_API_KEY not found. Please add your API key to the .env file."
    )

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "user", "content": args.user_prompt},
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
)

usage = response.usage

if usage is None:
    raise RuntimeError(
        "No token usage information was returned by the API."
    )

print(response.choices[0].message.content)

if args.verbose:
    print(
        f"User prompt: {args.user_prompt}\n"
        f"Prompt tokens: {usage.prompt_tokens}\n"
        f"Response tokens: {usage.completion_tokens}"
    )
