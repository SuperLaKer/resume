```
# 当用户登陆后，django会把request.user传给每个模板文件

# 如果用户登陆user是User类的实例
# 如果未登录，user是AnonymouseUser类的实例为None
```

```html
{% if user.is_authenticated %}  //user对象直接传递给模板文件
	<div class="login_btn fl">
		欢迎您：<em>{{ user.username }}</em>
		<span>|</span>
		<a href="{% url 'user:logout' %}">退出</a>
	</div>
{% else %}  //user为空，说明没有登陆
	<div class="login_btn fl">
		<a href="{% url 'user:login' %}">登录</a>
		<span>|</span>
		<a href="{% url 'user:register' %}">注册</a>
	</div>
{% endif %}
```

