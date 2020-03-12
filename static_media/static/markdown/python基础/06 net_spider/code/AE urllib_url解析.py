# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/4/28 15:28'
from urllib import parse

base_url = "https://www.baidu.com/s?wd=python&username=abc#1"
print(len(base_url))


# parse.urlparse(url)  131
def main0():  # 257 252
    result = parse.urlparse(base_url)

    # ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='',
    # query='wd=python&username=abc', fragment='1')
    print(result)

    print("scheme:", result.scheme)
    print("metloc:", result.netloc)
    print("path:", result.path)
    print("params:", result.params)
    print("query:", result.query)
    print("fragment:", result.fragment)


# parse.urlsplit(url)
def main(good):
    print(good)
    result = parse.urlsplit(base_url)

    print(result)

    print("scheme:", result.scheme)
    print("metloc:", result.netloc)
    print("path:", result.path)
    # print("params:", result.params)
    print("query:", result.query)
    print("fragment:", result.fragment)


# session保持cookie,github


if __name__ == '__main__':
    main()
