#### 概念

- 用户通过浏览器访问网站，使用redis记录用户信息比如：`session  静态文件等等`
- 如果`reids服务器突然挂了`，基于内存的`redis主服务器`里面的数据全没了
- 需要另一台 `redis从服务器`，备份主服务器的数据
- 从服务器只能读，不能写

#### 读写分离

- 从服务器读取数据，主服务器写数据
- 经统计，网站的读写比例是10:1
- 主服务器可以有多个从
- 从服务器也可以有多个从服务器

#### 配置

- 可以在同一台电脑上，也可以不在

- `/etc/reids/reids.conf``

- `sudo redis-server /etc/redis/redis.conf`

- `cp /etc/redis/redis.conf ./redis-slave.conf`  # 名字随意

  ```
  bind  ip
  port  # 如果是同一台电脑，最好不要一样
  slaveof <masterip><masterport>
  slaveof 127.0.0.1 6379
  sudo redis-server /etc/redis/redis-salve.conf
  ```

- 参看主从

- `redis-cli -h 127.0.0.1 -p 6379 -info Replition`

- `role:master`  # 主或从

- `connected_slaves:数量`  # 从服务器的数量

- `slave0:ip`  # 0号从服务器的ip和端口，在线情况等等

#### 数据操作

```
redis-cli -h 127.0.0.1  # 连接到主服务
keys *
set name xiaoming
redis-cli -h 127.0.0.2 6378  # 连接到从
keys *
"name"  # 自动备份

```

