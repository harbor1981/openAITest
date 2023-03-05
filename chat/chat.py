import json
import os
from pathlib import Path

import openai


import os
import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = "sk-HVmS11aASruIUqaqYnBUT3BlbkFJ0o1ANz9HC3CSxbg655b"
openai.api_key = "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"

model_engine = "gpt-3.5-turbo"
# model_engine = "text-davinci-003"
# prompt = "小学班主任每个学期都要给学生写评语。请你帮忙给某个小学生写一段评语，关键词是成绩优良、体育比较差"
prompt = "小学班主任每个学期都要给学生写评语。请你帮忙给某个小学生写一段不少于100个汉字的评语，关键词是成绩优良、体育比较差."

# Generate a response

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message)


