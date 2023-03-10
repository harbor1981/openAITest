import json
import os
from pathlib import Path

import openai


import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "gpt-3.5-turbo"
# model_engine = "text-davinci-003"
# prompt = "小学班主任每个学期都要给学生写评语。请你帮忙给某个小学生写一段评语，关键词是成绩优良、体育比较差"
prompt = "小学班主任每个学期都要给学生写评语。请你帮忙给某个小学生写一段不少于100个汉字的评语，关键词是成绩优良、体育比较差."

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=2,
    stop=None,
    temperature=0.8,
)

response = completion.choices[0].text
print(response)

