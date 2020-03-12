# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/5/1 14:36'

# import queue
import multiprocessing
import random
import time


def main0():
    q = multiprocessing.Queue(5)
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)
    # q.put(6)  # 阻塞

    print(q.empty())  # False
    print(q.full())  # True

    while q.empty() is False:
        print(q.get_nowait())  # 没有数据不会阻塞，但会抛出异常


def producer(name, food, q):
    for i in range(10):
        time.sleep(random.random())

        print("\033[31m%s\033[0m 生产了：%s" % (name, food + str(i)))
        q.put(food + str(i))


def consumer(name, q):
    while True:
        food = q.get()
        if food is not None:
            time.sleep(random.random())
            print("\033[32m%s\033[0m消费了：%s" % (name, food))
        else:
            return

    # 生产者消费者模型


def main():
    q = multiprocessing.Queue(10)

    p = multiprocessing.Process(target=producer, args=("worker", "包子", q))
    p.start()

    c = multiprocessing.Process(target=consumer, args=("consumer1", q))
    c.start()

    c1 = multiprocessing.Process(target=consumer, args=("consumer2", q))
    c1.start()

    p.join()  # 当感知到生产者完成之后
    q.put(None)
    q.put(None)


if __name__ == '__main__':
    main()
