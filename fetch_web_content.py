import requests
from bs4 import BeautifulSoup


def fetch_web_content(web_url):
    try:
        response = requests.get(web_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title')
        if title:
            return title.text
        else:
            return "网页没有标题标签"
    except requests.exceptions.RequestException as e:
        return f"请求出错：{e}"
    except Exception as e:
        return f"解析出错：{e}"


url = 'https://kimi.moonshot.cn/'
web_title = fetch_web_content(url)
print("网页标题: ", web_title)
