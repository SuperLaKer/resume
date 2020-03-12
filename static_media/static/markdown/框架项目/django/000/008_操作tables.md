```python
# python manage.py shell
# 从bookinfo包的models.py文件中导入BookInfo类
from bookinfo.models import BookInfo
```

```python
# 增
b = BookInfo()  # 创建类对象
b.tittle = '天龙八部'  # 给类属性赋值
from datetime import date
b.pub_date = date(1990,1,1)
b.save()  # 调用类方法（继承与models.Model）

# 查
b2 = BookInfo.objects.get(id=1)  # b2 是BookInfo的对象，查到的数据，保存在对象中
b2.btittle  # 对象.类属性  查看类属性的值

# 改（查到之后）
b2.bpub_date=date(1995,10,10)
b2.save()

# 删
b2.delete()  # id=1 那行数据被删除
```

```

```

