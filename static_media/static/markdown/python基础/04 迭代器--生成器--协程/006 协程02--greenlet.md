## greenlet实现多任务

```
pip install greenlet
```

```
# 使用greenlet
from greenlet import greenlet

import time


def test1():
    while True:
        print("--1 --")
        gr2.switch()  # 切换到test2
        time.sleep(0.1)


def test2():
    while True:
        print("--2--")
        gr1.switch()  # 切换到函数test1
        time.sleep(0.1)


gr1 = greenlet(test1)
gr2 = greenlet(test2)


def main():
    gr1.switch()


if __name__ == '__main__':
    main()
```

