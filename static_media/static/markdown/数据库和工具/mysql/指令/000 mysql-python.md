```
2.3 切换mysql数据库之后不能启动服务器
需要安装操作mysql数据库的包，python2环境和python3环境有以下区别。 
a)	python2需要安装mysql-python:
  pip install mysql-python
b)	python3需要安装pymysql:
  pip install pymysql
python3中安装好pymysql，需要在test2/__init__.py中加如下内容：
import pymysql
pymysql.install_as_MySQLdb()

```

