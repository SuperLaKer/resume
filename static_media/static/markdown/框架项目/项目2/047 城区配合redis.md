```
# 城区下拉框，频繁被访问
# 可以将查询到的 城区信息 保存 在一个全局变量中
# 将 城区信息 保存在redis中
```

```
# 流程
/area ==服务器==》访问：redis（没有）==》访问：mysql（必须有）===》存放到redis中==》返回给前端
```

```python
# 代码改写
api/house.py

@api.route("/areas")
def get_area_info():
    """获取城区信息"""
    # 尝试从redis中读取数据
    try：
    redis_store.get("area_info")
    except Exception as e:  # 有异常跳过else:
        current_app.logger.error(e)
    else:
        if resp_json is not None:
            # redis中有数据
            current_app.logger.info("hit redis area_info")
            return resp_json, 200, {"Content_Type": "application/json"}
    try:
    	area_li = Area.query.all()
    except Exception as e:
        current_app.logger.error(e)  # 记录日志
        return jsonify(errno="错误代码", errmag="数据库异常")
    area_dict_li = []
    # 在area中添加一个方法，用来将area转化成字典
    for area in area_li:
        area_dict_li.append(area.to_dict())
    # 将数据保存到redis中（不会修改）
    from ihome import redis_store
    # 将数据转换成字符串
    # errno="OK", errmsg="ok", data=area_dict_li
	resp_dict = dict(errno="OK", errmsg="ok", data=area_dict_li)
    resp_json = json.dumps(resp_dict)
    try:
        # redis缓存时间放在常量中
        redis_store.setex("area_info", constants.Area_info_redis_time, resp_json)

    return resp_json, 200, {"Content_Type": "application/json"}

```

数据库同步问题

```
# 给redis中的数据设置有效期
```

