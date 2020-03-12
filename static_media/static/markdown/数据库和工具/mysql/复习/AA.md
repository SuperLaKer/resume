```
默认数据库：
　　mysql - 用户权限相关数据
　　test - 用于用户测试数据
　　information_schema - MySQL本身架构相关数
```

#### 增删改查

```

```

#### 关于自增

```
MySQL的步长基于：会话，依次连接，下次登陆步长就变了
Sqlserver基于：表，创建表的时候指定步长
```

```sql
show session variables like 'auto_incx';  # 查看步长
set session auto_increment_increment=2;  # 设置步长

show session variables like 'auto_inc%';
set session auto_increment_increment=2;
set session auto_increment_offset=10;

shwo global  variables like 'auto_inc%';
set global auto_increment_increment=2;
set global auto_increment_offset=10;
```

#### 唯一，联合唯一

- 1和1，1和2，联合唯一：ok，唯一：error
- 多对多：联合唯一，根据情况

- 唯一：加速查找，可以为空
- 主键：不能为空，不能重复



#### 用户管理

```sql
create user '用户名'@'ip' identified by '密码';  # 创建用户和密码
rename user '旧的名字'@'ip'; to '新名字'@'ip';;  # 修改用户名
set password for '用户名'@'ip' = Password('新密码');
drop usere '用户名'@'ip';  # 删除用户

'用户名'@'IP地址'
'用户名'@'192.168.1.%'
'用户名'@'%'  # 
```

#### 权限

```sql
show grants for '用户名'@'ip';
grant 具体权限 on db_name.tb_name to '用户名'@'ip';  # 添加某项权限
revoke 具体权限 on db_name.tb_name for '用户名'@'ip';  # 废除某项权限

flush privileges;  # 生效

'数据库名'.'*'
'数据库名'.'表'
'数据库名'.'存储过程'
'*'.'*'
```

#### 具体权限

- 可以其他用户可以创建、删除、修改用户，但不能添加、更改权限

```sql
all privileges  除grant外的所有权限，不能给修改其他用户权限
select          仅查权限
select,insert   查和插入权限
            ...
usage                   无访问权限
alter                   使用alter table
alter routine           使用alter procedure和drop procedure
create                  使用create table
create routine          使用create procedure
create temporary tables 使用create temporary tables
create user             使用create user、drop user、rename user和revoke  all 

create view             使用create view
delete                  使用delete
drop                    使用drop table
execute                 使用call和存储过程
file                    使用select into outfile 和 load data infile
grant option            使用grant 和 revoke
index                   使用index
insert                  使用insert
lock tables             使用lock table
process                 使用show full processlist
select                  使用select
show databases          使用show databases
show view               使用show view
update                  使用update
reload                  使用flush
shutdown                使用mysqladmin shutdown(关闭MySQL)
super                   使用change master、kill、logs、purge、master和set 
replication client      服务器位置的访问
replication slave       由复制从属使用
```

