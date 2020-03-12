```
项目web_html.py

# 创建一个csrf_token值
    csrf_token = csrf.generate_csrf()

    # flask提供的返回静态文件的方法
    resp = make_response(current_app.send_static_file(html_file_name))

    resp.set_cookie("csrf_token", csrf_token)

    return resp
```

遗忘

```
# from flask import make_response
# flask设置cookie
# cookie不设置过期时间
```

