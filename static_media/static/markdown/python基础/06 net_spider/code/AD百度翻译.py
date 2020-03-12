# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/4/28 1:41'

import requests


def main():
    my_url = "http://m.iciba.com/index.php?c=search&m=getsuggest&nums=5&client=6&uid=0&is_need_mean=1" \
             "&=的" \
             "_=1556392469207&callback=jsonp9"
    request_header = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) "
                                    "AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    response = requests.get(my_url, request_header)

    content = response.content.decode()

    print(content)

    print(response.text)


if __name__ == '__main__':
    main()
