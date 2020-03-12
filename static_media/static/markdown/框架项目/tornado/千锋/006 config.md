- tornado,options.define("port")
- 值的获取方式
- tornado.options.parse_command_line()
- tornado.options.parse_config_file()
- 不支持字典

```
touch config

port = 7000
list = [good, better, best]
```



```
tornado.options.parse_config_file("config")

httpServer.bind(tornado.options.options.port)

```

