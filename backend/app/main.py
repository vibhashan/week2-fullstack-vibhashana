from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
from app.services import generate_service
from app.models.payload_model import Payload
from app.middlewares.error_handling_middleware import GlobalExceptionHandler

load_dotenv()

app = FastAPI()

# Register middlewares
app.add_middleware(GlobalExceptionHandler)


@app.get("/")
def root():
    return RedirectResponse("/health")


@app.get("/health", status_code=200)
def health():
    return "OK"


@app.post("/generate", status_code=200)
async def generate(payload: Payload):
    # TODO Add guardrails for topic
    result = await generate_service.generate(payload.input)
    return result
