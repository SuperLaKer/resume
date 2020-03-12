#### cookie

- 服务器怎么设置cookie到本地浏览器？
  - 获取的响应
- 

```python
timeout=3  等待三秒
retry  装饰器
method  设置请求方法


headers = {}


@retry(stop_max_attempt_number=3)  # 三次出错抛出异常
def _parse_url(url, method, data, proxies):
    print("*" * 20)
    if method == "POST":
        response = requests.post(url, data=data, headers=headers, proxies=proxies)

    else:
        response = requests.get(url, data=data, headers=headers, proxies=proxies)

    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, method="GET", data=None, proxies=None):
    try:
        html_str = _parse_url(url, method, data, proxies)
    except:
        html_str = None
    return html_str


if __name__ == '__main__':
    url = "http://www.baidussss.com"
    url1 = "http://www.baidu.com"

    print(parse_url(url1))
```

