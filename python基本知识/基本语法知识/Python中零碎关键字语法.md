## python中零碎关键字语法
### 1. if else 条件判断
* 简单示例：
````python
a = "abcd"
if a=="a":
    print("a")
elif a=="b":
    print("b")
else:
    print(a)

````
### 2. for ... in 循环
* 语法：for 变量名称 in 可迭代对象:
* 简单示例
````python
for i in range(5):
    print(i)
````
### 3. while 循环
* 语法： while 条件：循环体
* 简单示例
````python
a = 10
while a!=5:
    if a>100:
        break
    elif a>10:
        a -= 1
        continue
    else:
        print(a)
````
### 4. if else表达式
* 简单示例
````python
a = 10
b = 100 if a>5 else 0  #如果a的值大于5就将100返回，否则返回0
````
### 5. 解析式[]{}
* 解析式是立即求值
* 列表解析式
````python
lst = [i+1 for i in range(5)]  #等价于[1,2,3,4,5]
lst2 = [i for i in range(5) if i>2]  #等价于[3,4]
````
* 集合解析式
````python
set1 = {i+1 for i in range(5)}  #等价于{1,2,3,4,5}
````
* 字典解析式
````python
set2 = {i:i+1 for i in range(5)} #等价于{0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
````
### 6. 生成器表达式()
* 生成器表达式是惰性求值
* 简单示例
````python
lst = (i+1 for i in range(5))
next(lst)  #当lst获取到最后一个值后再次next会报错
````

### 7. lambda匿名函数
* 简单示例
````python
fn = lambda x,y=4: x+y
print(fn(5))  #返回值为9
print(fn(x=1,y=2)) #返回值为3
````
### 8. yield停止当前函数执行，通常用来创建生成器函数
* yield关键字，可以中断当前函数执行。如果函数中使用了yield 那么该函数一定是一个生成器函数
1. 简单示例：
    ````python
    def getNum():
    for i in range(5):
        yield i   #注意当执行时遇到yield语句，就暂停该函数的执行。并将yield后面的值返回。
    gnum = getNum() #生成器函数执行，会返回生成器对象。可迭代。

    for i in range(6):
        print(next(gnum)) # 注意，如果函数体执行完成，生成器的游标走到了末尾。会报StopIteration错误
    ````  
    ![yield001](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/yield001.jpg)  
### 9. yield from语法糖
* 从Python3.3开始增加了yield from语法.
* yield from就是一种简化的语法糖
* yield from iterable 等价于 for item in iterable : yield item
* 简单示例
````python
def sol():
    for i in [1,2,3]: yield i

def sol2():  #注意：sol2与sol效果等价
    yield from [1,2,3]
iterab = sol()
iterab2 = sol2()
print(next(iterab),next(iterab))
print(next(iterab2),next(iterab2))
````  
![yield003](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/yield003.jpg)   

### 10. with...as语法(上下文管理)
* 上下文管理：一种特殊的语法，交给解释器去释放文件对象  
* 使用with...as 关键字
* 上下文管理的语句块并不会开启新的作用域
* with语句块执行完的时候，会自动关闭文件对象
* 第一种写法示例：
````python
del f
#使用with...as 语法，当代码块中出现异常时，会自动关闭f
with open("test") as f:
    f.write("abc") #因为是只读模式打开，所有会出错。写入失败
#测试f发现f已经关闭
f.closed 
````
* 第二种写法：
````python
f = open("test")
with f:
    f.write("abcd") #因为是只读模式打开，所有会出错。写入失败
#测试f，f已经关闭
f.closed
````  
