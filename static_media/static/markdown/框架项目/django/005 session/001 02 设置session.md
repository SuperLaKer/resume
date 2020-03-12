```
设置session：request.session['username']=username
设置session：request.session['password']=password

获取session：request.session['passoword']
	request.session.get('键'， 默认值)  # 找不到使用默认值
	
清楚session
	request.session.clear()  # 只清除 值 的部分 base64解码
	
完全清除session：
	request.session.flush
	
指定删除：
	del request.sessionp["唯一标识码"]
```

```
服务器端：设置完session，会浏览器设置cookie（sessionid:唯一标识码）
```

```
django_session 

唯一标识码（主键）   session——date(保存的session数据：字典形式)

request.session['passoword']
```

## 设置过期时间

```
# 设置sessionid的过期时间 COOKIE, value整数：秒，0：关闭浏览器，None:两周后过期
request.session.set_expiry(value)
```

