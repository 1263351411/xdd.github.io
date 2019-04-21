# Python重点注意地方
### 例子1： 运算符号+=
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

### 例子2：切片赋值
````python
arr = [1,2,3,4,5,6,7,8,9,10] #定义一个列表
print("arr = {} \t id = {}".format(arr,id(arr)))
#arr[1:9:2] = ["a","b"]  #注意此时，会将arr中 2,4,6,8 删除，会出现4个空位。而插入的元素只有两个。会报错。
arr[1:9:2] = ["a","b","c","d"]  #会将arr中 2,4,6,8 删除。并在对应位置替换成a,b,c,d
print("arr = {} \t id = {}".format(arr,id(arr)))
````  
![slice11](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/slice11.jpg)  

### 例子3： 生成器表达式中的闭包
* 例子:1
````python
def getcont():
    key = 5
    hh = (key+i for i in range(4))
    key = 100  #注意此时生成器中的key对应的值会变成100
    return hh
hh = getcont()  ## 注意此时生成器中key对应的值变成100，形成闭包。
key = 120 #此时key与hh中生成器的key不同
list(hh)
````  
![yield005](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/yield005.jpg)  

* 例子2：  
````python
def add(n,i):
    return n+i

def test():   #生成器函数值为【0,1,2,3,】
    for i in range(4):
        yield i

g=test()
for n in [1,10]:
    g=(add(n,i) for i in g)   #定义生成器，其中生成器中n为标识符。注意：n为标识符，当循环执行完成后，局部变量中n的值为10
#     g = (add(n,i) for i in (add(n,i) for i in g) )
print(list(g))
````
![yield004](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/yield004.jpg)  