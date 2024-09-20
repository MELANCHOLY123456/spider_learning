import requests

response=requests.get('https://kimi.moonshot.cn/')

# response.status_code为200表示请求成功
print(response.status_code)
