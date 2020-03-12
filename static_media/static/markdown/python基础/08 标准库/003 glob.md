- glob是python自己带的一个文件操作相关模块

- 用它可以查找符合自己目的的文件
- 支持`* ? []`这三个通配符
- `*`代表0个或多个字符，?代表一个字符，[]匹配指定范围内的字符，如[0-9]匹配数字

```
import glob
path_list = glob.glob(r"D:\project\requirements\freeze_project03.txt")

# 返回值：文件路径列表
```

