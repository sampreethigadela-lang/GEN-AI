import os
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv(Path(__file__).with_name(".env"))

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found. Add it to the .env file beside main.py."
    )

client = genai.Client(api_key=api_key)

PREFERRED_MODEL = "gemini-3.8-flash"
PROMPT = "What is Artificial Intelligence? Explain in simple words."
TEMPORARY_ERROR_CODES = {429, 500, 502, 503, 504}


def generate_with_retries(model: str, attempts: int = 3):
    for attempt in range(attempts):
        try:
            return client.models.generate_content(model=model, contents=PROMPT)
        except errors.APIError as exc:
            if exc.code not in TEMPORARY_ERROR_CODES or attempt == attempts - 1:
                raise
            delay = 2 ** (attempt + 1)
            print(f"Gemini is temporarily unavailable; retrying in {delay} seconds.")
            time.sleep(delay)


try:
    response = generate_with_retries(PREFERRED_MODEL)
except errors.APIError as initial_error:
    if initial_error.code not in TEMPORARY_ERROR_CODES | {404}:
        raise

    print(f"{PREFERRED_MODEL} is unavailable. Checking available Gemini Flash models.")
    try:
        available_models = client.models.list()
    except errors.APIError as exc:
        raise RuntimeError(
            "Could not check available Gemini models. Verify your API key and try again."
        ) from exc

    fallback_models = []
    for model_info in available_models:
        name = model_info.name or ""
        model_name = name.removeprefix("models/")
        actions = model_info.supported_actions or []
        if (
            model_name
            and model_name != PREFERRED_MODEL
            and "flash" in model_name.lower()
            and "generateContent" in actions
        ):
            fallback_models.append(model_name)

    if not fallback_models:
        raise RuntimeError(
            "No alternative Gemini Flash model supporting text generation is available."
        ) from initial_error

    response = None
    for model_name in fallback_models[:3]:
        try:
            response = generate_with_retries(model_name, attempts=2)
            print(f"Using available model: {model_name}")
            break
        except errors.APIError as exc:
            if exc.code not in TEMPORARY_ERROR_CODES | {404}:
                raise

    if response is None:
        raise RuntimeError(
            "Gemini Flash models are currently unavailable. Please try again later."
        ) from initial_error

print("\nLLM Response:")
print(response.text or "The model returned no text.")