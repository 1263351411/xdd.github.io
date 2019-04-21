## tuple元组,命名元组namedtuple
#### 元组的定义和初始化
* 定义：由一个有序的元素组成的集合。元组是**不可变**对象
    * tuple()->empty tuple 返回一个空元组
        * ()也可以定义一个空元组。
        * (1,)表示是由一个元素1组成的元组
        * tuple()是工厂方法，
    * tuple(iterable)-> tuple 根据可迭代对象返回一个新元组
#### 元组查询
* index(value,[start,[stop]])通过值value，从指定区间查找元组中value值对应的索引，如果没找到会抛出ValueError异常
    * value 需要查找的值
    * start 查找的起始索引
    * stop 查找的结束索引
    * 注意：时间复杂度为O(n)
* count(value) 返回列表中匹配value的次数，时间复杂度为O(n)
    * value 需要匹配的值。
####元组的其他操作
* 元组是只读的，所以没有增、删、改方法
* len(tuple) 返回元素的个数
#### 命名元组namdtuple
* namedtuple(typename,field_names,verbose=False,rename=False) 命名元组，返回一个元组的子类，并定义了字段
    * typename 类名（自己随便定义，要符合命名规则）
    * field_names 可以是空白字符或逗号分割的字段的字符串，可以是字段的列表(相当于定义typename的属性列表)
* 简单示例No1
````python
from collections import namedtuple
Point = namedtuple("_Point",['x','y']) #Point为返回的类，_Point为返回类的类名
pt1 = Point(1,2)
print(pt1,pt1.x,pt1.y,sep="\t")
````
![tuple0001](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/tuple0001.jpg)  
* 简单示例No2
````python
from collections import namedtuple
Student = namedtuple("_Student","name,age sex like")
stud1 = Student("张三",15,"男","打篮球")
print(stud1,stud1.name,stud1.age,stud1.sex,stud1.like,sep="\n")
````   
![tuple0002](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/tuple0002.jpg)  