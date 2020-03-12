### 设置Cookie

```python
使用HttpResponse类对象，或是它的子类的对象(HttpResponseRedirect, JsonRespone)
设置cookie：set_cookie方法
读取Cookie：request.COOKIES
```

```python
def set_cookie(request):
    """设置cookie信息"""
    response = HttpResponse("设置cookie")
    # 设置cookie信息。名字为num,值为1
    response.set_cookie('num', 1)

    return response
```

### 读取cookie

```python
def get_cookie(request):
    """获取cookie"""
    # 取出cookie num的值
    num = request.COOKIES['num']
    return HttpResponse(num)
```

