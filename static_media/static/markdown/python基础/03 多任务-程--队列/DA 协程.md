#### 协程

#### 使用协程和栈、队列

- 本质上是一个线程，在一个线程中实现并发效果
- 能够规避一些任务中的IO操作
- 在任务的执行过程中，检测到IO就切换到其他任务
- 使用场景：
  - 高IO操作
  - 爬虫
  - socket_server

#### yield

- 不能规避IO操作时间
- 函数的跳转

```
def consumer():
	while True:
		x = yield
		print("处理了数据：%s" % x)

def producer():
	c = consumer()
	next(c)
	for i in range(10):
		print("生成了数据：%s" % i)
		c.send(i)
def main():
	producer()  # 调用函数
```

#### greenlet

```

```

