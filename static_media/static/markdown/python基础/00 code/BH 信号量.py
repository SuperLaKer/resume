# 信号量：对代码加锁，某一时间只能有几个线程可以使用
# 互斥锁：threading.Lock()
# 递归锁：threading.RLock()


from threading import Semaphore, Thread, Lock, RLock
import time


def main(sem, a, b):
    sem.acquire()
    time.sleep(1)
    print("{}+{}".format(a, b))
    print("")
    sem.release()


if __name__ == "__main__":
    sem = Semaphore(2)  # 同时允许两个线程执行某些代码
    for i in range(10):
        Thread(target=main, args=(sem, i, i * 11)).start()
        # 主线程等待子线程执行结束
