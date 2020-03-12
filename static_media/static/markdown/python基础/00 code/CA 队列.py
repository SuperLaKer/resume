# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/5/2 18:00'

import queue


# 队列
def demo():  # 先进先出
    q = queue.Queue()
    q.put()
    q.get()
    q.put_nowait()  # full error
    q.get_nowait()  # empty error


# 栈
def demo2():  # 先进后出
    q = queue.LifoQueue()


# 优先队列
def demo3():
    q = queue.PriorityQueue()
    q.put((20, "b"))
    q.put((10, "a"))
    q.put((5, "b"))
    q.put((5, "a"))  # a优先级高

    print(q.get())


if __name__ == '__main__':
    demo3()
