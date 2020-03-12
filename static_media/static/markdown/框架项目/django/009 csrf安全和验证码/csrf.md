```
在<form>表单中添加一个模板标签
{% csrf_token %}
渲染时：{% csrf_token %}被替换为<input type="hideden" name="csrfmiddlewaretoken" value="一堆">
返回页面的同时：服务器设置一个cookie
key：csrf
value:"一堆"
```

```
不同客户端的csrf的value:"一堆" 不一样
提交时：form表单和cookie也会别提交
比较成功就ok了
```

