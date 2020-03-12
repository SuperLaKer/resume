#### 标准

```
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader， RequestContext(类)
```

```python
def index(reqest):
    # 加载模板文件(相对于tempaltes文件加)(template/booktest/index.html)
    temp = loader.get_template(booktest/index.html)
    # 定义模板上下文：给模板传数据（模板变量）
    context = RequestContext(request, {'变量'： '值'})
    # 模板渲染（把模板变量换成值）产生标准html内容
    res_html = temp.render(context)
    # 返回给浏览器
    return HttpResponse(res_html)
	# render(request, 'booktest/index.html'，{})
```

#### 封装(render的来历)

```python
def my_render(request, template_path, context_dict={}):
        # 加载模板文件(相对于tempaltes文件加)(template/booktest/index.html)
    temp = loader.get_template(template_path)
    # 定义模板上下文：给模板传数据（模板变量）
    context = RequestContext(request, context_dict)
    # 模板渲染（把模板变量换成值）产生标准html内容
    res_html = temp.render(context)
    # 返回给浏览器
    return HttpResponse(res_html)
```

