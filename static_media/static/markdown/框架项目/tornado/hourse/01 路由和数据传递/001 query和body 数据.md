## 传参方式

- 对于请求体数据为`json或xml`的，无法通过这两个方法获取。请求体（body）
- 请求体中的数据要求为字符串
- 且格式为表单编码格式：即`key1=value1&key2=value2`
- HTTP报文头Header中的`Content-Type`为`application/x-www-form-urlencoded `或 `multipart/form-data`



- self.get_query/body_argument("name")`  取出最后一个
- `self.get_query/body_arguments("name")`  全部取出放到`list`中
- `self.get_argument/s("name")`  # 整合取出来body和url路径

```
# /index?key=value&k2=v2&k2=key2  可以同名get(name)取最后一个、gets(name)全取放到list中
# /subject/(python)
# cookie
# header
```

```python
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # subject = self.get_query_argument("subject", "default")  # 覆盖前面的subject=
        subject = self.get_query_arguments("subject")  # 全部放到list中

        self.write(str(subject))

    def post(self, *args, **kwargs):
        data = self.get_body_argument("b")
        datas = self.get_body_arguments("b")
        self.write(str(datas))
```

## 思考

1. 什么时候设置default，什么时候不设置default？

   如：性别

2. default的默认值_ARG_DEFAULT是什么？

   全局唯一

3. 什么时候使用strip，亦即什么时候要截断空白字符，什么时候不需要？

   需求