#### 注意区分，作为转发nginx和web服务器

```
[uwsgi]
#使用nginx连接时使用
socket=127.0.0.1:8080
#直接做web服务器使用
#http = 127.0.0.1:8889
#项目目录
chdir = /media/lla/APP/code/resume
#项目中wsgi.py文件的目录，相对于项目目录
wsgi-file = resume/wsgi.py
processes = 2
threads = 2
master = True
pidfile = uwsgi.pid
daemonize = uwsgi.log
virtualenv = /root/code/resume/static
```

```
location / {
    include uwsgi_params;
	uwsgi_pass 127.0.0.1:8889;
}
location /static {
	# 指定静态文件存放路径
}

```

```
uwsgi --ini uwsgi.ini  # 启动uwsgi
uwsgi --stop uwsgi.pid
```

#### Windows服务器

```

```

