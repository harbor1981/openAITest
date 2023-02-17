import json
import os
from pathlib import Path

import openai

PROMPT = "a white siamese cat"
DATA_DIR = Path.cwd() / "responses"

DATA_DIR.mkdir(exist_ok=True)

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "sk-HVmS11aASruIUqaqYnBUT3BlbkFJ0o1ANz9HC3CSxbg655b"

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json",
)

file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"

with open(file_name, mode="w", encoding="utf-8") as file:
    json.dump(response, file)
