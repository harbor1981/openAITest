#-*- coding: UTF-8 -*-
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "gpt-3.5-turbo"
# model_engine = "text-davinci-003"
prompt = "小学班主任每个学期都要给学生写评语。请你帮忙给某个小学生写一段评语，关键词是上课爱讲话、体育比较差"
# prompt = "小学班主任每个学期都要给学生写评语。请你帮忙给某个小学生写一段不少于100个汉字的评语，关键词是成绩优良、体育比较差."
# 1
# Generate a response

completion = openai.ChatCompletion.create(
  model=model_engine,
  messages=[
    {"role": "user", "content": prompt}
  ]
)
result=completion.choices[0].message.content
print(prompt)
print(result)
print("ok")

