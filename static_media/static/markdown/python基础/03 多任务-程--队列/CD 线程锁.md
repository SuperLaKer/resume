```python
import threading

lock = threading.Lock()

lock.acquire()  # 拿钥匙
print("拿到了")
lock.acquire()  # 又拿钥匙，阻塞
print("拿到了too")
```

#### 死锁

- `from threading import mutex`
- `lock = multex.Lock()`
- 在同一个线程中如果需要两把以上的锁，容易产生死锁
- 可以使用`rlock`, `from threading import rlock`