# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/5/1 21:46'

import multiprocessing


def test(n):
    print(n ** 3)


def main_map():
    x = map(test, [1, 2, 3, 4])

    for i in x:  # 返回计算后的结果
        print(i)


def main_pool():
    pool = multiprocessing.Pool(4)

    pool.map(test, [2, 3, 4, 5, 6])


if __name__ == '__main__':
    main_pool()
