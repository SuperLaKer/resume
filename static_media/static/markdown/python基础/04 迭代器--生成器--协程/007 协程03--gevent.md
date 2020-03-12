```
import gevent
from gevent import monkey
import time
monkey.patch_all()


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)  # 打印个gevent对象
        # gevent.sleep(0.1)
        time.sleep(1)


g1 = gevent.spawn(f, 5)  # spawn卵
g2 = gevent.spawn(f, 5)  # 关联函数，传入参数
g3 = gevent.spawn(f, 5)  # 创建gevent对象

g1.join()  # 等待
g2.join()
g3.join()

print("*"*10)

gevent.joinall([gevent.spawn(f, 5), gevent.spawn(f, 5), gevent.spawn(f, 5)])
```

