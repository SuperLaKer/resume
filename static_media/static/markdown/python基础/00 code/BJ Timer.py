# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/5/2 17:48'

import threading


def test():
    print("同步时间")


clock = threading.Timer(2, test)
clock.start()  # 异步
