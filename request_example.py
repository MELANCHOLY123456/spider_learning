import requests

response = requests.get('https://kimi.moonshot.cn/')

# response.status_code为200表示请求成功
print(response.status_code)

# 改进版
try:
    response = requests.get('https://www.xiaohongshu.com/', timeout=10)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"请求失败，状态码：{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"请求出错：{e}")
