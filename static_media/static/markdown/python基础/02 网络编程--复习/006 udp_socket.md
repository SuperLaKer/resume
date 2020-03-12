### udp

#### 基本通讯过程

- 创建套接字
- 收发数据
- 关闭套接字

#### 没有消息应答

- 发送数据后：没有反馈，不知道数据是否传输成功

#### UDP

- `UDP:User Datagram Protocol`
- 在[网络](https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C)质量令人十分不满意的环境下，UDP协议数据包丢失会比较严重
- 它不属于连接型协议，因而具有资源消耗小，处理速度快的优点
- 偶尔丢失一两个数据包，也不会对接收结果产生太大影响
- 聊天用的ICQ和[QQ](https://baike.baidu.com/item/QQ)就是使用的UDP协议

```
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 tcp 套接字对象
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp套接字对象
# 使用套接字

# 关闭套接字
s.close()
```

