# Gemini AI Quick Start

This project is a simple Python application that uses the Google Gemini API to generate a response to a prompt.

The script loads your API key from a local `.env` file, selects a Gemini model, and prints the generated answer in the terminal.

## Project structure

- `main.py` – main application logic
- `requirements.txt` – Python dependencies
- `.env` – local environment variables (not committed)

## Features

- Reads `GEMINI_API_KEY` from `.env`
- Connects to the Google GenAI client
- Tries the preferred Gemini Flash model first
- Falls back to another available Gemini Flash model if needed
- Retries temporary API failures automatically
- Prints the final generated response

## Requirements

- Python 3.10+
- A valid Google Gemini API key

## Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your API key:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

## Run the project

```bash
python main.py
```

The script sends this prompt:

```text
What is Artificial Intelligence? Explain in simple words.
```

and prints the model response to the console.

## Notes

- The script uses model fallback logic for Gemini Flash models, which helps if the preferred model is unavailable.
- Temporary errors such as rate limits and server issues are retried automatically.
- Make sure your API key is valid and has access to the Gemini API.

## License

This project is provided for educational and learning purposes.
