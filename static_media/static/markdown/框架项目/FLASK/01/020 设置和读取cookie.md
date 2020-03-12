参考代码

```
07_cookie.py
```

```
from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    resp.set_cookie("cookie_name", "cookie_value")
    resp.set_cookie("cookie2_name", "cookie2_value")
    resp.set_cookie("cookie3_name", "cookie3_value", max_age=3600)

    return resp


@app.route("/get_cookie")
def get_cookie():
    c = request.cookies.get("cookie3")
    return c


if __name__ == '__main__':
    app.run(debug=True)
```

