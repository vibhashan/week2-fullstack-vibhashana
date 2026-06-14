from pydantic import BaseModel


class Result(BaseModel):
    title: str
    summary: str
