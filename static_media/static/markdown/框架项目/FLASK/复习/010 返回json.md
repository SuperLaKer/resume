#### json就是字符串

- 数据结构转化为字符串，不仅仅是字典
- 字符串转化为python的数据结构

```python
data = {"": "", "": ""}

import json
json_str = json.dumps(data)

dict_data = json.loads(json_str)
```

```python
@app.router("/index")
def index():  # 使用全局的request
	data = {
		"": "",
		"": ""
	}
	json_data = json.dumps(data)
	return json_data, 200, {"Content-Type": "application/json"}
```

```python
from flask import jsonify
@app.router("/index")
def index():  # 使用全局的request
	data = {
		"": "",
		"": ""
	}
	return jsonify(data)  # 两个作用：转化为json,设置相应头
```

```
from flask import jsonify
@app.router("/index")
def index():  # 使用全局的request

	return jsonify(name="slk", browser="chorme")  # 不用传字典，直接传递键值对
```

