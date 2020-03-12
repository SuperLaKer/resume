#### 计算代码运行时间

```
import time
start_time = time.time()
end_time = time.time()
```

#### timeit模块

- Timer是测量小段代码执行速度的类。

- stmt：参数是要测试的代码语句（statment）；

- setup：参数是运行代码时需要的设置；

- timer：参数是一个定时器函数，与平台有关

```
# 创建一个Timer
class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)
# 测试次数，float类型的秒数
timeit.Timer.timeit(number=1000000)
```

```
def test1():
   l = []
   for i in range(1000):
      l = l + [i]

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "seconds")
```

