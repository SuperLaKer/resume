```python
from flask import Flask

app = Flask(__name__)

@app.route("/login")
def login():
    # 设置session数据
    session["name"] = "python"
    session["mobile"] = "18611111111"
    return "login success"

def index():
    
```

