```python
# 登陆校验视图
def login_check(request):
    # 1、获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')  # 记住用户名
    # print(remember)  none  on
    # 2、进行登陆验证
    if username == 'smart' and password == '123':
        if remember == 'on':  # 登陆成功 并且 用户名和密码对了
            rem = HttpResponse()  # 设置cookie
            rem.set_cookie('username', username, max_age=3600)
        return redirect('/index')
    else:
        return redirect("/login")
```

```python
# 登陆页面
def login(request):

    if 'username' in request.COOKIES:  # 是否有保存相关cookie
        field = request.COOKIES['username']
    else:
        username = ''
    return render(request, 'booktest/login.html', {'username': str(field)})
```

```html
/*login页面*/
<form method="post" action="/login_check">
    用户名：<input type="text" name="username" value="{{ username }}">
    <input type="checkbox" name="remember">记住用户<br/>
    密码：<input type="password" name="password"><br/>
    <input type="submit" value="登陆">
</form>
```

