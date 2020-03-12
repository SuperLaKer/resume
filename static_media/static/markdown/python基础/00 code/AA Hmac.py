# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/5/1 0:21'

import os
import time
from multiprocessing import Process


class Myprocess(Process):
    def __init__(self, person):
        super().__init__()
        self.person = person

    def run(self):
        print(os.getpid(), self.name)
        time.sleep(2)
        print('%s正在和女主播聊天' % self.person)


if __name__ == '__main__':
    p = Myprocess('哪吒')
    p.daemon = True  # start前设置，主结束子结束
    p.start()
    # Myprocess('哪吒').start()
    p.join()  # 主等待子

    print('主')
