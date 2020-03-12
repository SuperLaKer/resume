```
密码直接加密：加密密码 = sha1(密码)
密码混淆加密：加密密码 = sha1(密码+混淆字符串)  # 盐值
数据库存储方式：混淆字符串%加密密码

登陆(重新加密，如果和数据库中的密码一样就登陆成功了)
sha1(密码 + 混淆字符串)
```

```python
# 密码逻辑实现
# 在类中添加一个方法：需要穿进去密码，把密码加密然后直接把加密结果给类属性（数据库column数据）

def generate_password_hash(self, origin_password):
    """对密码进行加密"""
    //给类属性赋值
    self.password_hash = generate_password_hash(origin_password)
	
```

#### property装饰器

```python
class User(BaseModel, db.Model):
    
    @property  //（读取方法）加上property装饰器后，函数变成了属性user.password = (返回值xxx)
    def password(self):
        """读取属性的函数行为"""
        return "xxx"  //函数的返回值会作为属性值
    
    @password.setter  //设置方法，
    def password(self, origin_password):
        self.password_hash = generate_password_hash(origin_password)
    
    
# 可读取函数返回值：print(user.password)
# 也可给函数赋值：user.password = value

```

