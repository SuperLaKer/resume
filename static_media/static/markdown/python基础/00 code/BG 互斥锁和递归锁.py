import threading
import time


def main0():
	lock = threading.Lock()

	lock.acquire()  # 拿钥匙
	print("拿到了")
	lock.acquire()  # 又拿钥匙，阻塞
	print("拿到了too")

NUM = 0

def worker(lock):
	global NUM
	for n in range(1000000):
		lock.acquire()
		NUM += 1
		lock.release()
	print("worker ", NUM)

def worker1(lock):
	global NUM
	for n in range(1000000):
		lock.acquire()
		NUM += 1
		lock.release()
	print("worker1 ", NUM)

def main():
	lock = threading.Lock()

	threading.Thread(target=worker, args=(lock, )).start()
	threading.Thread(target=worker1, args=(lock, )).start()

	time.sleep(5)



def main2():
	from threading import Rlock
	# 使用rlock同时对多个数据加锁，就不会产生互斥的现象了


if __name__ == "__main__":
	main()