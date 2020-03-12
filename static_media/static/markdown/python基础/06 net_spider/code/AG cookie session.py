# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/4/28 17:33'

import requests


# 获取cookies
def main0():
    my_url = "https://www.baidu.com"
    response = requests.get(my_url)

    print(response.cookies)  # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
    print(type(response.cookies))  # <class 'requests.cookies.RequestsCookieJar'>
    # 使用实例方法：转化成字典
    print(response.cookies.get_dict())  # {'BDORZ': '27315'}


# session保持cookie,github
def main():
    # 数据准备
    data = {"username": "superlaker", "password": "github"}
    my_tuple = (1, 2, 3)

    print(my_tuple)
    form_url = ""

    my_header = {"": ""}

    # 创建session对象
    ssion = requests.session()

    # session对象发送post请求
    ssion.post(form_url, data=data, headers=my_header)

    # session对象，get访问我的关注
    profile_url = ""
    response = ssion.get(profile_url)
    print(response.content.decode())


class User(object):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    main()
