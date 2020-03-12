- 当管理员更新首页数据时，对应的模型管理类中的save()、delete()方法会自动执行
- 模型在后台注册admin.py中，如果没有指定管理类，会自定使用django的ModelAdmin
- 自定义类，继承与admin.ModelAdmin
- 修改后save()会自动调用
- 重写save(),
- 再调用super().save(dddd)，完成修改
- 然后是，celery的任务代码
- 修改数据后，管理员无须等待celery
- 便可直接退出
- celery会重新生成静态界面

```python
# 代码源
apps.goods.admin
# 第五行代码开始

```

