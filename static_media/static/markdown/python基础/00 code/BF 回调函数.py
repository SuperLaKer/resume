__author__ = "superlaker"
__date__ = '2019/5/1 22:59'

import multiprocessing
import threading
import time
import os


def test(n):
    for i in range(5):
        time.sleep(0.8)
        print("%s" % n, os.getpid(), threading.current_thread())


def main_process():
    p = multiprocessing.Process(target=test, args=(u"子进程",))
    p.start()
    p2 = multiprocessing.Process(target=test, args=(u"守护进程",))
    p2.daemon = True
    p2.start()
    time.sleep(2)
    print(u"主进程代码结束")


def main_threading():
    threading.Thread(target=test, args=(u"子线程", )).start()
    t = threading.Thread(target=test, args=(u"守护线程",))
    t.daemon = True
    t.start()


def sub_test():
    print("你好")


if __name__ == '__main__':
    main_threading()
