import json
import os
from pathlib import Path

import openai


import os
import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = "sk-HVmS11aASruIUqaqYnBUT3BlbkFJ0o1ANz9HC3CSxbg655b"
openai.api_key = "sk-DrinZx8hOc4SQvpXOA6LT3BlbkFJLaPpQq9pcqnEtIkV3eiC111"

model_engine = "text-davinci-003"
prompt = "小学班主任每个学期都要给学生写评语。请你帮忙给某个小学生写一段不少于100个汉字的评语，关键词是成绩优良、体育比较差"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)

