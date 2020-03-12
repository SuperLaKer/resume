# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/5/1 22:36'

import multiprocessing
import time


def func(n):
    time.sleep(0.2)
    return "---%s---" % n


if __name__ == '__main__':
    p = multiprocessing.Pool(2)

    for i in range(10, 20):
        result = p.apply(func, args=(i,))  # apply的结果就是函数的返回值
        print(result)

    print("*" * 50)
    res_list = []
    for i in range(10, 20):
        result = p.apply_async(func, args=(i,))  # apply的结果就是函数的返回值
        # print(result.get())  # 阻塞等待计算结果
        res_list.append(result)  # 拿到所有的结果对象

    print(res_list)  # <multiprocessing.pool.ApplyResult object at 0x0000028CAA7B0160>
    for rest in res_list:
        print(rest.get())  # 取出结果
