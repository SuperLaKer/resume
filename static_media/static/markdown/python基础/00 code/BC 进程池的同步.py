# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/5/1 22:12'

import os
import time
import random
import multiprocessing


def func(n):
    print("start func %s" % n, os.getpid())
    time.sleep(random.random())
    print("enddd func %s" % n, os.getpid())


if __name__ == '__main__':
    p1 = multiprocessing.Pool()
    p2 = multiprocessing.Pool(2)
    for i in range(10):  # 循环添加10个任务
        p1.apply(func, args=(i,))  # apply默认是前一个执行完，再添加另外一个任务

    print("*" * 100)

    for ii in range(10, 20):
        p2.apply_async(func, args=(ii ** 2, ))

    p2.close()  # 不再接收任务，才能拿使用join感知
    p2.join()  # error 进程池中的进程不会结束，用完了还回去



