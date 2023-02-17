import openai

# 设置 API Key，申请地址：https://platform.openai.com/account/api-keys.E
openai.api_key = 'sk-HVmS11aASruIUqaqYnBUT3BlbkFJ0o1ANz9HC3CSxbg655b'
# 设置组织，查看地址：https://platform.openai.com/account/org-settings
# openai.organization = "xmu"
# 请求模型
model_engine = "text-davinci-002"
# 输入内容
prompt = "给某个小学生写期末评语，关键词是勤奋和学习待提升。一段话就好，中文，不超过100个字"
# 调用接口
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
# 输出结果
message = completions.choices[0].text
print(message)

