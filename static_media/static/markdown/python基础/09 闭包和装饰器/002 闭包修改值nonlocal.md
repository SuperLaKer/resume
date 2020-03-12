```python
x = 100
def demo():
    x = 200
    def demo1():
        nonlocal x  # 说明函数中的x来自外界
        print("--%d--" % x)  # 输出 200
        x = 300
        print("--%d--" % x)  # 输出 300
        
    return demo1  # 返回引用
        
        
t1 = demo()
print("--%d--" % x)  # 输出 100
```



定义函数跳过

return：t1====>demo1