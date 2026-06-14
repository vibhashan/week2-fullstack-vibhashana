from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def root():
    return RedirectResponse("/health")


@app.get("/health", status_code=200)
def health():
    return "OK"
