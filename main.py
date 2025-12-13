import os 
from dotenv import load_dotenv
from google.genai import (
    client,
    types
) 
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY") 

if api_key == None:
    raise RuntimeError("API key could not be found")

client = client.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")

parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")

args = parser.parse_args()
# Now we can access `args.user_prompt`

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

response = client.models.generate_content(
    model='gemini-2.5-flash', contents=messages
)

if response.usage_metadata == None:
    raise RuntimeError("No usage metadata, probably bad request")

if args.verbose:
    print(f"""
    User prompt: {args.user_prompt}
    Response tokens: {response.usage_metadata.candidates_token_count}
    Prompt tokens: {response.usage_metadata.prompt_token_count}
    Response: {response.text}
          """)
else:
    print(response.text)
