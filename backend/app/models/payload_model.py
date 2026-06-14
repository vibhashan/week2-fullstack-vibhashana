from pydantic import BaseModel


class Payload(BaseModel):
    input: str
    model: str
