# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/4/29 19:03'

import re
import requests


def main():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    response = requests.get("https://duanziwang.com/page/5/", headers=headers)

    print(response.status_code)

    my_str = response.content.decode()

    context_list = re.findall("<p>(.*?)</p>", my_str)

    print(context_list)

    # with open("text.txt", "a", encoding="utf-8") as f:
    #     f.write(str(context_list))
    #
    # print(str(context_list))


def main1():
    my_str = ".".join(["1", "2", "3"])
    print(my_str)


if __name__ == '__main__':
    main1()
