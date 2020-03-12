```python
def extend_list(val, a_list=[]):
    a_list.append(val)
    return a_list  # 这里不是print

def main():
    list1 = extend_list(10)  # 默认[].append(10)

    list2 = extend_list(123, [])  # 传进去的[].append(123)

    list3 = extend_list("a")  # 默认追加a [10].append("a")

    print(list1, "\n", list2, "\n", list3)
    # result is :  [10, "a"], [123], [10, "a"]
```

- 知识点：集合

- python中如何书写可变参数和默认参数？
  - `*args  默认参数（默认参数放到后面）`
- `*args和**kwargs什么时候使用？`
  - 不确定有多少个参数。分别接收：位置参数，关键字参数
- python删除文件？
  - `import os  os.remove()`