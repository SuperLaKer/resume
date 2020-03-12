# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/5/1 16:57'

from multiprocessing import Pipe, Manager, Process, Lock


def main():
    conn1, con2 = Pipe()

    conn1.send("conn1_send")
    print(con2.recv())

    con2.send("conn2_send")
    print(conn1.recv())  # str


def work(d, lock):
    with lock:  # 不加锁而操作共享的数据,肯定会出现数据错乱
        d['count'] -= 1


if __name__ == '__main__':
    lock = Lock()
    m = Manager()
    dic = m.dict({'count': 100})
    p_l = []
    for i in range(50):
        p = Process(target=work, args=(dic, lock))
        p_l.append(p)
        p.start()
    for p in p_l:
        p.join()
    print(dic)
