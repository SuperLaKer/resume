from greenlet import greenlet
import time


def test1():
	print("test1")
	g2.switch()  # 函数执行完接不执行了，需要使用for来回切换

def test2():
	print("test2")
	g1.switch()


if __name__ == "__main__":

	g2 = greenlet(test2)
	g1 = greenlet(test1)

	g1.switch()

