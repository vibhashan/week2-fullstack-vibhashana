import requests
import os
from dotenv import load_dotenv

load_dotenv()

FAST_API_BASE_URL = os.getenv("FAST_API_BASE_URL").rstrip("/")


def call_backend(path: str, payload: dict):
    # Using requests.Session() handles connections more efficiently
    with requests.Session() as session:
        response = session.post(f"{FAST_API_BASE_URL}{path}", json=payload, timeout=10)

        return response
