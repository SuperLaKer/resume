#### 设置cookie和session

- session保存在服务端，由服务端设置，
- 使用包含用户数据的request直接设置

- cookie有浏览器设置，设置在响应头中，浏览器解析，然后设置
- 就需要使用HttpResponse的对象设置，整合在响应头中

```python
def set_sesson(request):
    """设置session"""
    request.session['username']='skjd'
    request.session['age']=18
    return HttpResponse('设置session')
```

```python
def set_cookie(request):
    """设置cookie信息"""
    response = HttpResponse("设置cookie")
    # 设置cookie信息。名字为num,值为1
    response.set_cookie('num', 1)

    return response("设置cookie")
```

