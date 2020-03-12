#### uwsgi

遵循wsgi协议的web服务器

##### 安装

```
pip install uwsgi
```

##### 配置setting.py

```python
DEBUG=FALSE
ALLOWED_HOSTS=['*']
```

配置文件

```python
# 根目录新建uwsgi.ini

# 直接使用uwsgi做web服务器
http=127.0.0.1:8000

# 项目目录
chdir=Users/slk/Desktop/dailyfresh

# 项目中wsgi.py文件的目录，相对于项目目录
wsgi-file=dailyfresh/wsgi.py

processes=4
threads=2

# 主进程
master=True
# 保存主进程的pid
pidfile=uwsgi.pid
# 设置uwsgi为后台进程，保存日志
daemonize=uwsgi.log
# 设置虚拟环境的路径
virtualenv=/Users/slk/.virtualenvs/dailyfresh

```

##### 启动和停止

```
启动：uwsgi --ini 配置文件路径（相对一项目目录） uwsgi --ini uwsgi.ini
停止：uwsgi --stop uwsgi.pid路径  例如：uwsgi --stop uwsgi.pid
```

