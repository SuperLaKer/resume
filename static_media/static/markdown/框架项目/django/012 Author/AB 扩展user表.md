## 扩展默认的auth_user表

- `auth_user`表字段都是固定的那几个，无法满足开发需求
- 通过继承内置的 `AbstractUser` 类，来定义一个自己的Model类。
- 既能根据项目需求灵活的设计用户表，又能使用Django强大的认证系统了
- 一旦我们指定了新的认证系统所使用的表，我们就需要重新在数据库中创建该表，而不能继续使用原来默认的auth_user表了，迁移

#### 重要

```
# 引用Django自带的User表，继承使用时需要设置
AUTH_USER_MODEL = "app名.UserInfo"
```

- 自定义认证系统默认使用的数据表之后，我们就可以像使用默认的auth_user表那样使用我们的UserInfo表了

- 创建普通用户：类名.objects.

  ```
  UserInfo.objects.create_user(username='用户名', password='密码')
  ```

- 创建超级用户

  ```
  UserInfo.objects.create_superuser(username='用户名', password='密码')
  ```

  