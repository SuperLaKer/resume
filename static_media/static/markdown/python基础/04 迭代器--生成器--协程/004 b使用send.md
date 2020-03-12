```python
# 使用next()获取特殊迭代器的值
obj = gen()
next(f)

# 使用send()
obj = gen()
obj.send("返回值")
```

```python
def send_xxx():  # 使用send取值
    obj = create_num(10)  # 同一个obj对象

    result = next(obj)
    print(result)  # 0

    result = obj.send("yield_return_value")  # 右边必须执行完成
    print(result)  # 1


if __name__ == '__main__':
    send_xxx()
```

