1. session默认保存在sql数据库中
2. 新建django项目
3. 应用注册
4. 修改数据库配置
5. urls设置
6. 模板目录配置
7. 静态文件配置

cookie

- 浏览器的cookie的key和value：sessionid:唯一标识码
- 服务器的session两个字段：唯一标识码：session数据

#### redis配置

```
pip install django-redis-sessions==0.5.6
```

```python
# sesson默认存放位置，默认在sql数据库，这里更改为redis
SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = 'localhost'
SESSION_REDIS_PORT = 6379
# 使用那个数据库（0-15）
SESSION_REDIS_DB = 2
SESSION_REDIS_PASSWORD = '921166'
# 服务器生成session会有唯一标识码
# （session:标识码）这一堆作为key
# get (session:标识码)
SESSION_REDIS_PREFIX = 'session'
```

#### 设置session

```python
def set_sesson(request):
    """设置session"""
    request.session['username']='skjd'
    request.session['age']=18
    return HttpResponse('设置session')


def set_sesson(request):
    """设置session"""
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username+':'+str(age))
```

这样就存在了redis中了，而不会存在mysql数据库中

```
keys * 
"session:唯一标识码"--->这一坨作为key，值就是设置的data
```

