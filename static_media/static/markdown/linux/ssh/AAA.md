## SSH服务

ssh（security shell,安全外壳协议），该协议有两个作用：远程链接、远程文件传输

协议默认使用端口：默认是22

配置文件：`etc/ssh/ssh_config`

#### 安装

```
apt install openssh-server
service ssh start
ps -e |grep ssh
```

