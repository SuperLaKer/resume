# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/5/2 18:11'
"""
ThreadPoolExecutor:线程池，提供了异步调用
ProcessPoolExecutor:进程池，提供异步调用
拥有相同的接口函数
submit(fn, *args, **kwargs)
map(func, *iterables, timeout=None, chunksize=1) 取代for循环submit的操作


"""
from concurrent.futures import ThreadPoolExecutor
import time


def worker(n):
    time.sleep(1)
    print(n)
    return n * 11


def callback(n):
    print("结果是%s" % n.result())


def main():
    tpool = ThreadPoolExecutor(max_workers=5)
    # result_list = []
    for i in range(20):
        # result = tpool.submit(worker, i)
        tpool.submit(worker, i).add_done_callback(callback)
    # result_list.append(result)

    tpool.shutdown()

    # for result in result_list:
    #     print(result.result())

    print("主进程结束")


if __name__ == "__main__":
    main()
