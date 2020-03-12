#### 相应

```python
from flask import make_response

@app.router("/index")
def index():  # 使用全局的request
	resp = make_response("index page2")  # response对象
	resp.status = "666 ok"
	resp.headers["user"] = "slk"
	return resp
```

#### 设置cookie

```python
from flask import make_response

@app.router("/set_cookies")
def index():  # 使用全局的request
	resp = make_response("设置cookie")
	resp.set_cookie("cookie_name", "cookie_value")  # 临时cookie
	resp.set_cookie("cookie_name", "cookie_value", max_age=3600)  # 单位：秒
```

#### 获取cookie

```python
# 所有数据都在request中
@app.router("/get_cookies")
def index():  # 使用全局的request
	my_cookie = request.cookies.get("cookie_name")
	return my_cookie
```

#### 删除cookie

- 本质：设置cookie马上过期
- 因为：JavaScript不能读写客户端数据

```python
from flask import make_response

@app.router("/delete_cookies")
def index():  # 使用全局的request
	resp = make_response("删除cookie")
	resp.delete_cookie("cookie_name")
	
```

#### 原理

本质：设置响应头

```python
Set-Cookie: BD_CK_SAM=1;path=/


from flask import make_response

@app.router("/index")
def index():  # 使用全局的request
	resp = make_response("index page2")  # response对象
	resp.status = "666 ok"
	resp.headers["user"] = "slk"
	resp.headers["Set-Cookie"] = "BD_CK_SAM=1;path=/"  # 就是这样
	return resp
```

## session

- http请求是没有状态的
- 会话机制：存放状态信息
- flask需要配置：security_key
- 如果没有cookie可以将session设置到url中，重定向，添加session信息
- 设置在url中关闭浏览器，就不能保存信息了

#### 设置session

```python
def login():
	username = request.form.get("name")
	password = request.form.get("password")
	# 判断用户名和密码
	# 保存session，保存状态
	session["name"] = username
	。。。
	return "login success"  # 登陆成功，并保存session，一定时间内免密码登陆
```

#### 获取session

```python
def index():
	name = session.get("name")
	if name is not None: 
		user_id = session.get("user_id")  # 等等逻辑
	return "你刚才已经登陆，本次登陆不需要使用密码"  # 达到了保持回话状态的作用
```

