```python
# login
request.session['islogin'] = True
request.session.set_expiry(0)  # 关闭浏览器清除登陆状态
```

#### session 依赖cookie,   

key = sessionid, value = {'islogin': 'True'}

```python
# login_check
if request.session.has_key('islogin'):
	return redirect('/index')
else:
	# 是否记住了用户名
	# 返回登陆页面

```

