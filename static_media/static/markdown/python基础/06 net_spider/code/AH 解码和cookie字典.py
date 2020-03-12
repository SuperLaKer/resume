# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/4/29 15:01'
import requests


# 获取cookie，转化为字字典
def main0():
    url = "https://www.baidu.com"

    response = requests.get(url)
    print(response.status_code)

    cookie = response.cookies  # cookiejar对象
    # 方法一
    my_dict = cookie.get_dict()
    print(my_dict)
    # 方法二
    cookie_dict = requests.utils.dict_from_cookiejar(cookie)
    print(cookie_dict)
    # 相反方法
    my_cookiejar = requests.utils.cookiejar_from_dict(my_dict)
    print(my_cookiejar)


#  url编解码
def main():
    url = "https://www.baidu.comf?kw=帝吧"
    url_encode = requests.utils.quote(url)
    print(url_encode)  # https%3A//www.baidu.comf%3Fkw%3D%E5%B8%9D%E5%90%A7

    # url 解码
    url_decode = requests.utils.unquote("https%3A//www.baidu.comf%3Fkw%3D%E5%B8%9D%E5%90%A7")
    print(url_decode)


if __name__ == '__main__':
    main()
