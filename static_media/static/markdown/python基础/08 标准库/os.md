这个模块中的大部分函数通过对应平台相关模块实现, 比如 posix 和 nt.os
模块会在第一次导入的时候自动加载合适的执行模块.

```
import os.path
path = '/home/zikong/doc/file.doc'
print(os.path.basename(path))    # 查询路径中包含的文件名
print(os.path.dirname(path))     # 查询路径中包含的目录
print(__file__)
os.path.dirname(__file__)
os.path.abspath(__file__)

info = os.path.split(path) s      # 将路径分割成文件名和目录两个部分，放在一个表中返回
path2 = os.path.join('\', 'home', 'zikong', 'doc', 'file.doc')  #使用目录名和文件名构成一个路径字符串

p_list = [path, path2]
print(os.path.commonprefix(p_list))    # 查询多个路径的共同部分

os.path.normpath(path) # 去除路径path中的冗余。比如'/home/vamei/../.'被转化为'/home'
#os.path还可以查询文件的相关信息(metadata)。文件的相关信息不存储在文件内部，而是由操作系统
#维护的，关于文件的一些信息(比如文件类型，大小，修改时间)。

import os.path 
path = '/home/vamei/doc/file.txt'

print(os.path.exists(path))    # 查询文件是否存在

print(os.path.getsize(path))   # 查询文件大小
print(os.path.getatime(path))  # 查询文件上一次读取的时间
print(os.path.getmtime(path))  # 查询文件上一次修改的时间

print(os.path.isfile(path))    # 路径是否指向常规文件
print(os.path.isdir(path))     # 路径是否指向目录文件
```

