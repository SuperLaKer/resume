# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/5/1 15:58'

from multiprocessing import Process
from multiprocessing import JoinableQueue
import time
import random


def Worker(q):
    for i in range(10):
        time.sleep(random.random())

        print("worker---" + str(i))
        q.put(i)
    q.join()


def Consumer(q):
    while True:
        time.sleep(0.1)
        timer = str(q.get())
        print("Haver---" + timer)
        q.task_done()


def main():
    q = JoinableQueue(10)
    w = Process(target=Worker, args=(q,))
    w.daemon = True
    w.start()

    c = Process(target=Consumer, args=(q,))
    c.daemon = True
    c.start()
    w.join()


if __name__ == '__main__':
    main()
