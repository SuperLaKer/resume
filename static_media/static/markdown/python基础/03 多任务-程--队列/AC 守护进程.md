进程之间是相互独立的，主进程代码执行结束，不会影响代码中创建的其他进程

#### 守护进程

守护进程类比于协程了，主结束子结束

子进程：会随着主进程的结束而结束。

#### 创建守护进程

- 主进程创建守护进程
- 守护进程会在主进程代码执行结束后就终止
- 守护进程内无法再开启子进程,否则抛出异常：AssertionErro
- 进程之间是互相独立的，主进程代码运行结束，守护进程随即终止

```python
import os
import time
from multiprocessing import Process

class Myprocess(Process):
    def __init__(self,person):
        super().__init__()
        self.person = person
    def run(self):
        print(os.getpid(),self.name)
        time.sleep(2)
        print('%s正在和女主播聊天' %self.person)


p=Myprocess('哪吒')
p.daemon=True # start前设置，主结束子结束，主等待子
p.start()
print('主')
```

