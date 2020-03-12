## form表单

- 在HTML页面中利用form表单向后端提交数据时，都会写一些获取用户输入的标签并且用form标签把它们包起来。
- 好多场景下都需要对用户的输入做校验，比如校验用户是否输入，输入的长度和格式等正不正确
- 如果用户输入的内容有错误就需要在页面上相应的位置显示对应的错误信息.

- Django form组件就实现了上面所述的功能

#### form组件的主要功能如下:

- 生成页面可用的HTML标签
- 对用户提交的数据进行校验
- 保留上次输入内容

```python
# views.py定义类
from django import forms

# 按照Django form组件的要求自己写一个类
class RegForm(forms.Form):
    name = forms.CharField(label="用户名")
    # name = forms.CharField()
    pwd = forms.CharField(label="密码", max_length=16)
```

```python
# 使用form组件实现注册方式
def register2(request):
    form_obj = RegForm()
    if request.method == "POST":
        # 实例化form对象的时候，把post提交过来的数据直接传进去
        form_obj = RegForm(request.POST)
        # 调用form_obj校验数据的方法
        if form_obj.is_valid():
            return HttpResponse("注册成功")
    return render(request, "register2.html", {"form_obj": form_obj})
```

```html
	<form action="/register2/" method="post" novalidate autocomplete="off">
        {% csrf_token %}
		{{ form_obj.as_p }}
		<p><input type="submit"></p>
    </form>
```

```html
	<form action="/register2/" method="post" novalidate autocomplete="off">
        {% csrf_token %}
        <div>
            <label for="{{ form_obj.name.id_for_label }}">{{ form_obj.name.label }}</label>
            {{ form_obj.name }} {{ form_obj.name.errors.0 }}
        </div>
        <div>
            <label for="{{ form_obj.pwd.id_for_label }}">{{ form_obj.pwd.label }}</label>
            {{ form_obj.pwd }} {{ form_obj.pwd.errors.0 }}
        </div>
        <div>
            <input type="submit" class="btn btn-success" value="注册">
        </div>
    </form>
```

```python
def register(request):
    error_msg = ""
    if request.method == "POST":
        username = request.POST.get("name")
        pwd = request.POST.get("pwd")
        # 对注册信息做校验
        if len(username) < 6:
            # 用户长度小于6位
            error_msg = "用户名长度不能小于6位"
        else:
            # 将用户名和密码存到数据库
            return HttpResponse("注册成功")
    return render(request, "register.html", {"error_msg": error_msg})
```

```html
<form action="/reg/" method="post">
    {% csrf_token %}
    <p>
        用户名:
        <input type="text" name="name">
    </p>
    <p>
        密码：
        <input type="password" name="pwd">
    </p>
    <p>
        <input type="submit" value="注册">
        <p style="color: red">{{ error_msg }}</p>
    </p>
</form>
```

