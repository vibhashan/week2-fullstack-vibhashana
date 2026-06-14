import json
from openrouter import OpenRouter
from app.models.result_model import Result
import os


async def generate(input: str):
    # TODO Improve error handling
    with OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY")) as client:
        result = await client.chat.send_async(
            model="openrouter/free",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    You are a helpful assistant that generates a title and a summary based on user input. The title
                    must not be greater than 10 words and the summary must be at least 50 words.

                    Input: {input}
                    """,
                },
            ],
            # TODO Implement streaming
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "result",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "summary": {"type": "string"},
                        },
                        "required": ["title", "summary"],
                        "additionalProperties": False,
                    },
                },
            },
        )

        result_dict = json.loads(result.choices[0].message.content)

        return Result(title=result_dict["title"], summary=result_dict["summary"])
