```
request：包含浏览器请求信息
```

```
from django.http.request import QueryDict
QueryDict
request.POST


q = QueryDict('a=1&b=2&c=3')
取值：q['a']  键不存在抛出异常
取值：q.get('c')  键不存在不报错
q.get('b', 'default')
```

```
request.POST.get("password")
```

```
request.method
request.path:一个字符串，表示请求的页面的完整路径，不包域名和参数部分
requese.file:一个类似于字典的对象，包含所有上传文件
COOKIES：一个标准的python字典，包含所有cookie，键和值都为字符串
session：可读可写、类似于字典的对象
```

