# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/5/2 16:46'

import threading


def worker(key, ii):
    key.acquire()
    key.wait()
    print("在第%s个循环里" % ii)
    key.release()


def main():
    keys = threading.Condition()

    for i in range(10):
        threading.Thread(target=worker, args=(keys, i)).start()  # 开启10个线程，等待钥匙

    while True:
        num = int(input("请数据整型数字：\n"))  # error

        keys.acquire()
        # keys.notify(int(input("请数据整型数字：\n")))  # error
        keys.notify(num)
        keys.release()


if __name__ == "__main__":
    main()
