# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/4/27 13:25'

import requests


# 百度图标
def main0():
    # 发送请求
    urls = "https://www.baidu.com/img/bd_logo1.png"

    response = requests.get("https://www.baidu.com/img/bd_logo1.png")

    print(response.status_code)

    with open("D:\\code\\baidu.png", "wb") as f:
        f.write(response.content)  # content 是二进制数据，text是字符串


# content 和 text
def main1():
    urls = "https://www.sina.com.cn"

    response = requests.get(urls)

    print(response.status_code)

    print(response.content.decode())
    #
    # response.encoding = "utf-8"
    # print(response.text)


# 常用的方法和断言
def main2():
    response = requests.get("https://www.baidu.com")

    print(response.status_code)  # 如果从定向了，也是200，但不是同一个url地址

    try:
        assert response.status_code == 200
    except Exception:
        pass  # 添加到列表，查看那些请求失败了
    else:
        print("请求成功")
        print(response.url)
        print(response.headers)
        print(response.request.url)
        print(response.request.headers)

        print(response.content.decode())


# 添加请求头
def main3():
    header_dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    response = requests.get("https://www.baidu.com", headers=header_dict)  # 设置请求头

    # 设置了请求头，相应的body内容和浏览器一样
    print(response.content.decode())

    print(response.request.headers)


def main():
    header_dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    url_search = "https://www.baidu.com/s?wd=python"  # 百度搜索ok

    url = "https://www.baidu.com/s?"

    search = "wd=python"

    response = requests.get("https://www.baidu.com", headers=header_dict)  # 设置请求头

    # 设置了请求头，相应的body内容和浏览器一样
    print(response.content.decode())

    print(response.request.headers)


if __name__ == '__main__':
    main()
