# 关系模型和SQL

为了介绍关系模型，以MySQL数据为例。

* 安装MariaDB

````shell
#安装mariadb
> yum install mariadb-server
#启动服务
> systemctl start mariadb.service
#开机启动
> systemctl enble mariadb.service
# 为了安全设置Mysql服务
> mysql_secure_installation
# 数据库密码登录
> mysql -u root -p
# 显示所有数据库
mysql> show databases;
# 创建用户并授权
mysql> grant all on *.* to 'xdd'@'%' identified by 'xdd';
mysql> flush privileges;
# 导入测试脚本
> mysql -u root -p < test.sql
````

## SQL语句

* SQL是结构化查询语言Structured Query Language。1987年被ISO组织标准化。  
* 所有主流的关系型数据库都支持SQL，NoSQL也有很大一部分支持SQL。

* SQL语句分为：
    1. **DCL数据库控制语言**
        * 负责数据库权限访问控制，由GRANT和REVOKE两个指令组成
    2. **DDL数据定义语言**
        * 负责数据库定义，数据库对象定义，由CREATE,ALTER与DROP三种语句组成
    3. **DML数据库操作语言**
        * 负责对数据库对象的操作，CRUD增删改查
    4. **TCL事务控制语言**
        * 负责处理ACID事务，支持commit、rollback指令

* 语言规范
    1. SQL语句大小写不敏感
        * 一般建议，SQL的关键字、函数等大写
    2. SQL语句末尾应该使用分号结束
    3. 注释
        * 多行注释 `/*注释内容*/`
        * 单行注释 `-- 注释内容`
        * MySQL注释可以使用#
    4. 使用空格或缩进来提高可读性
    5. 命名规范
        * 必须以字母开头
        * 可以使用数字、#、$和_
        * 不可使用关键字

## DDL命令

## DCL数据库控制语言

GRANT授权，REVOKE撤销  

````slq
GRANT ALL ON employees.* TO 'xdd'@'%' IDENTIFIED by 'xdd';
REVOKE ALL ON *.* FROM xdd;
````

1. 常用特殊符号
    * `*`为通配符，代指任意库或者任意表。
    * `*.*`所有库的所有表。
    * `employess.*`表示employees库下所有的表
    * `%`为通配符，它是SQL语句的通配符，匹配任意长度字符串

## DDL数据库定义语言










