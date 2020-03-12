# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/5/1 1:13'

import os
import time
import random
from multiprocessing import Process, Lock


def work(lock, n):
    lock.acquire()
    print('%s: %s is running' % (n, os.getpid()))
    time.sleep(random.random())
    print('%s:%s is done' % (n, os.getpid()))
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(3):
        p = Process(target=work, args=(lock, i))
        p.start()
