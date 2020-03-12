#### abort函数

```
# 主动终止代码执行
# 返回给前端一些信息
# 传递给前端状态码信息
abort(404)
abort(400)
# 必须是标准的http状态码
```

传递响应体信息

```
resp = Response("login failed")
abort(resp)
```

