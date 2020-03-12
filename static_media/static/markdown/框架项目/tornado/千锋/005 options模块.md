## options 定义变量

- tornado,options.define("port")
- 值的获取方式
- tornado.options.parse_command_line()
- tornado.options.parse_config_file()
- 不支持字典

```python
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define("port", default=8000, type=int)
tornado.options.define("list", default=[], type=str, multiple=True)
# tornado.options.parse_command_line()
# python d_options.py --port="8080"  --list=1,2,3


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello tornado")
        
if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    httpServer = tornado.httpserver.HTTPServer(app)

    tornado.options.parse_command_line()  # 从命令行获取参数, 默认的会被覆盖
    # tornado.options.options  # 所有定义的选项变量，都会作为该变量的属性
    httpServer.bind(tornado.options.options.port)
    httpServer.start(2)

    tornado.ioloop.IOLoop.current().start()
```

```
tornado.options.define()
"""
    name: str,   变量名字，唯一性error:Option already define
    default: Any = None,  设置选项变量的默认值，默认为None
    type: type = None,  设置类型 port:int,命令行或配置文件导入，自动转换类型"8000" ---> 8000,转换不成报错
    
    
    help: str = None,  选项变量的帮助提示信息
    metavar: str = None,
    multiple: bool = False,  选项变量是否可以为多个值
    group: str = None,
    callback: Callable[[Any], None] = None,
"""
```

