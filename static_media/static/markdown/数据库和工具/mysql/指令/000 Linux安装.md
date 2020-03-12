安装

```
sudo apt-get install mysql-server
sudo mysql_secure_installation  # 配置

# 修改密码
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';
```

卸载

```
dpkg --list|grep mysql
sudo apt-get remove mysql-common
sudo apt-get autoremove --purge mysql-server
dpkg --list|grep mysql
sudo apt-get autoremove --purge mysql-apt-config

# sudo apt remove mysql-server-5.7
# rm -rf /etc/mysql
```



```
 select host,user from mysql.user;
```

```
/etc/init.d/mysql stop
```

```
delete from user where User="slk";
```

创建用户

```
insert into mysqy.user(Host,User,Password)values("localhost","root","password(123456)");
```

