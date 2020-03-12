## JSON

- JSON 指的是 JavaScript 对象表示法（JavaScript Object Notation）
- JSON 是轻量级的文本数据交换格式
- JSON 简单的语法格式和清晰的层次结构明显要比 XML 容易阅读

- 书写简单，一目了然；符合 JavaScript 原生语法，可以由解释引擎直接处理，不用另外添加解析代码。
- 属性名必须使用双引号
- .

JavaScript 对象和 JSON 字符串相互转化　

```
JSON.parse('{"name":"Q1mi"}');
JSON.stringify({"name":"Q1mi"})
```

## AJAX

- 异步的Javascript和XML
- 使用Javascript语言与服务器进行异步交互，传输的数据为XML（不只是XML）
- 异步交互：客户端发出一个请求后，无需等待服务器响应结束，就可以发出第二个请求。
- AJAX请求无须刷新整个页面；
- 因为服务器响应内容不再是整个页面，而是页面中的部分内容，所以AJAX性能高； 

## jQuery实现的AJAX

```
$("#b1").on("click", function () {
    $.ajax({
      url:"/ajax_add/",
      type:"GET",
      data:{"i1":$("#i1").val(),"i2":$("#i2").val(),"hehe": JSON.stringify([1, 2, 3])},
      success:function (data) {
        $("#i3").val(data);
      }
    })
  })
```

## JS实现AJAX

```
var b2 = document.getElementById("b2");
  b2.onclick = function () {
    // 原生JS
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", "/ajax_test/", true);
    xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttp.send("username=q1mi&password=123456");
    xmlHttp.onreadystatechange = function () {
      if (xmlHttp.readyState === 4 && xmlHttp.status === 200) {
        alert(xmlHttp.responseText);
      }
    };
  };
```

## AJAX请求如何设置csrf_token

- 如果使用从cookie中取csrftoken的方式，需要确保cookie存在csrftoken值。
- 如果你的视图渲染的HTML文件中没有包含 {% csrf_token %}，Django可能不会设置CSRFtoken的cookie。
- 这个时候需要使用ensure_csrf_cookie()装饰器强制设置Cookie

```
django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def login(request):
    pass
```

```
$.ajax({
  url: "/cookie_ajax/",
  type: "POST",
  data: {
    "username": "Q1mi",
    "password": 123456,
    "csrfmiddlewaretoken": $("[name = 'csrfmiddlewaretoken']").val()  // 使用jQuery取出csrfmiddlewaretoken的值，拼接到data中
  },
  success: function (data) {
    console.log(data);
  }
})
```

```
$.ajax({
  url: "/cookie_ajax/",
  type: "POST",
  headers: {"X-CSRFToken": $.cookie('csrftoken')},  // 从Cookie取csrftoken，并设置到请求头中
  data: {"username": "Q1mi", "password": 123456},
  success: function (data) {
    console.log(data);
  }
})
```

```
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
```

```
function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});
```

```
https://www.cnblogs.com/liwenzhou/p/8718861.html
```

