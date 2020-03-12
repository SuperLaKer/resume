GIL

- `threading.current_thread()`  # 线程id，get_pid()一样的
- 不同的线程名字和不同的线程id
- `threading.active_count()`  # 活跃的线程数，应该sleep一下等待函数结束：子+主
- `threading.enumerate()`  # 返回活跃的线程id的list包括主线程

进程：主等待子，马上关掉守护

线程：主等待子，马上关掉守护，如果有子，则不会关闭守护

- 线程之间，代码数据文件是共享的，有独有的寄存器和栈
- 

