import requests

# 调用 DALL-E API 生成图像
prompt = "Generate an image of a cat wearing a hat"
model = "image-alpha-001"
key="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"
response = requests.get(f"https://api.openai.com/v1/images/generations", params={
    "model": model,
    "prompt": prompt
}, headers={
    "Authorization": f"Bearer {API_KEY}"
})

# 解析响应结果
data = response.json()
image_url = data['data'][0]['url']

# 保存图像
response = requests.get(image_url)
open("cat_with_hat.jpg", "wb").write
