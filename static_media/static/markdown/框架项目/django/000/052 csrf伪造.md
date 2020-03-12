```
只要有post请求，就加上{% csrf_token %}
这是一个隐藏的<input  >
```



- 登陆正常网站之后，你的浏览器保存了sessionid，你没有退出
- 不小心访问了另外一个网站，并且点击了页面上的按钮
-  跨站请求伪造
- django默认开启了CSRF防伪，只针对post方式
- 开启后会把用户的请求也限制了
- 所以有了csrf_token

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSRF</title>
</head>
<body>
<form method="post" action="/change_pwd_action">
    {% csrf_token %}
    新密码：<input type="password" name="pwd">
    <input type="submit" value="确认修改">
</form>
</body>
</html>
```

