## python中零碎关键字语法
#### yield停止当前函数执行，通常用来创建生成器函数
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
#### yield from语法糖
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

#### with...as语法(上下文管理)
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
