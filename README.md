# Synthetix

## What it does

A full-stack application that generates titles and summaries from user input using AI models via OpenRouter API. The backend uses FastAPI to handle requests and communicate with OpenRouter, while the frontend uses StreamLit to provide an interactive user interface for inputting text and selecting AI models.

## How to run it

Live demo: https://week2-fullstack-vibhashana-2026.streamlit.app/

To run locally:

### Prerequisites

- Python 3.12 or higher

### Steps

1. At repo root (`week2-fullstack-vibhashana/`), create a python virtual environment using `python -m venv .venv`
2. Ensure the virtual environment is activated via `.venv/Scripts/activate` (Windows) or `source .venv/bin/activate` (Linux/Mac). Check Python interpreter path via `Get-Command python` (Windows) or `which python` (Linux/Mac) to ensure it's using the one in the virtual environment. Run the command `python -m pip install --upgrade pip` to upgrade pip
3. Open a terminal in `backend` folder and install dependencies with `pip install -r requirements.txt`. Do the same in the `frontend/app` folder.
4. Create a `.env` file in the `backend/` folder and add your OpenRouter API key: `OPENROUTER_API_KEY=your_api_key_here`. Run the backend with `fastapi dev` and it'll be accessible at `http://127.0.0.1:8000`
5. Create a `.env` file in the `frontend/` folder and add the backend URL: `FAST_API_BASE_URL=http://127.0.0.1:8000`
6. In `frontend/app/` folder, run the frontend with `streamlit run main.py` and it'll be accessible at `http://localhost:8501`

## Tools used

- **Backend**: FastAPI
- **Frontend**: StreamLit
- **API**: OpenRouter for AI model integration
- **Deployment**: Streamlit Cloud (frontend) and Vercel (backend)

## What I learned

Both FastAPI and StreamLit were new technologies that were tried out. I learned how to build a full-stack application with a REST API backend and a web-based frontend, integrating with external AI services through structured API calls. I would consider improving the following aspects in the future:

- Better error-handling of the overall application
- Add guardrails for the user input and model output
- Add tests for the backend and frontend
- Add observability capabilities
