# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/4/28 15:08'

# request网络请求相关
from urllib import request
# 编解码模块
from urllib import parse


# url中文部分编码
def main0():
    my_dict = {'name': '张三', 'age': 18}
    result = parse.urlencode(my_dict)
    print(result)

    base_url = "https://www.baidu.com/s?wd=刘德华"  # 有中文无法访问
    # result1 = request.urlopen(base_url)  # error
    # print(result1.getcode())  # error

    my_url = "https://www.baidu.com/s?"
    my_url_encode = my_url + parse.urlencode({"wd": "刘德华"})  # 经过ur编码后
    result1 = request.urlopen(my_url_encode)

    print(my_url_encode)

    print(result1.getcode())


# url解码
def main():
    base_url = {"wd": "刘德华"}

    ret = parse.urlencode(base_url)  # only 键值对
    print(ret)

    result = parse.parse_qs(ret)
    print(result)


if __name__ == '__main__':
    main()
