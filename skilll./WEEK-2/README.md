# LLM Provider CLI

A command-line app that sends a prompt to either Google's Gemini API or a locally running Ollama model.

## Requirements

- Python 3.9 or later
- For Gemini: a Gemini API key
- For Ollama: [Ollama](https://ollama.com/) installed and running, with the `llama3.2` model available

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. To use Gemini, create a `.env` file in the project directory and add your API key:

   ```text
   GEMINI_API_KEY=your_api_key
   ```

   Keep this key private and do not commit the `.env` file.

4. To use Ollama, start Ollama and make sure the model is installed:

   ```powershell
   ollama pull llama3.2
   ```

## Run

Start the app:

```powershell
python main.py
```

Choose `gemini` or `ollama` when prompted, then enter your question.

## Tests

Run the unit tests with:

```powershell
python -m unittest
```
