#### 事物

#### 开启事务

```sql
begin;
sql语句;  # 暂时保存在数据库
sql语句;
sql语句;
sql语句;
rollback;  # 回滚，信息全部删除

begin;
sql语句;  # 数据库中会生成相关的信息
sql语句;
sql语句;
sql语句;
commit;  # 提交，永久性保存
```

#### 事物中创建保存点

```
begin;  # 不会全部回滚
sql语句1；
sql语句2；
savepoint sql2；  # 设置保存点
sql语句3；
sql语句4；
savepoint sql4;  # 再次设立保存点

rollback to sql2;  # 回滚，后面删除
```

