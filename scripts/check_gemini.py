"""Check that the Gemini key and model work. Run from the project root."""
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()  # reads the .env file into environment variables

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL")

if not api_key or api_key == "paste_your_key_here":
    raise SystemExit("GEMINI_API_KEY is missing in .env")
if not model_name:
    raise SystemExit("GEMINI_MODEL is missing in .env")

print("Key found in .env (not shown).")
print("Model from .env:", model_name)

client = genai.Client(api_key=api_key)

# 1. Is the model name valid for this key?
available = [m.name.replace("models/", "") for m in client.models.list()]
print("Models visible to this key:", len(available))
if model_name in available:
    print("OK: model name exists.")
else:
    print("WARNING: model name not in the list. Similar names:")
    for name in available:
        if "flash-lite" in name:
            print("  ", name)

# 2. Make one tiny real call
response = client.models.generate_content(
    model=model_name,
    contents="Reply with exactly: Gemini is working",
)
print("Model replied:", response.text)