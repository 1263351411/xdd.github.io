# Python中与其他语言不通之处总结
####例子一： 运算符号+=
* 特殊注意，可变引用类型的+=：
````python
a = [1]
b = [2]
a += b  #等价于a.extend(b)
````
````python
def x(a=[],b="ab",c={3,5},d=(1,)):
    a += [5]  # 注意 a += [5] 等价于 a.extend([5])
    b += "cd"
    d += (2,) # 注意：元组tuple和字符串都是不可变类型
    #c += {4,6} #报错，集合不能这样用
print(x.__defaults__)
x()
x()
print(x.__defaults__)
````  
![fun003](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/fun003.jpg)