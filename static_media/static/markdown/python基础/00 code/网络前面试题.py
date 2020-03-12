def func(x, l=[]):
	print("l的地址是：", id(l))
	for i in range(x):
		l.append(i*i)
	print(l)

def main1():
	func(2)
	func(3, [3, 2, 1])
	func(3)

def main():
	a = []
	b = a

	print(id(a))
	print(id(b))

	a.append(1)
	print(a)
	print(b)


 



if __name__ == "__main__":
	main1()