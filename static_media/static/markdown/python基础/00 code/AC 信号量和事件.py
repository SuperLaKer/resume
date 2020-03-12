# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/5/1 1:27'
"""
e = Event()
print(e.is_set)
e.set()
e.clear()
e.wait()
红绿灯应用
"""

import time
import random
import threading


class Test(object):
    COUNT = 3

    def __init__(self):
        self.e = threading.Event()

    def check_web(self):
        time.sleep(random.random())
        self.e.set()

    def connect_db(self):
        while Test.COUNT > 0:
            self.e.wait(0.2)  # 超时为0.8秒，然后往下执行,极少连接失败
            if self.e.is_set():
                print("成功连接")  # 成功连接后return
                return
            else:
                print("超时")
            Test.COUNT -= 1
        print("数据库连接异常")

    def run(self):
        threading.Thread(target=self.check_web).start()
        threading.Thread(target=self.connect_db).start()


if __name__ == "__main__":
    Test().run()
    print("")
    print("当前线程数", threading.active_count())
