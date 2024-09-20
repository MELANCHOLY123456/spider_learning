from bs4 import BeautifulSoup
import requests

try:
    response = requests.get('https://github.com', timeout=10)
    response.raise_for_status()  # 检查状态码是否为200
    soup = BeautifulSoup(response.text, 'html.parser')
    if soup.title:
        print(soup.title.text)
    else:
        print("网页中没有找到<title>标签")
except requests.exceptions.RequestException as e:
    print(f"请求出错：{e}")
except Exception as e:
    print(f"解析出错：{e}")
