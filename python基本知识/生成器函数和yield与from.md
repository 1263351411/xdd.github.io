# 生成器函数和yield与from
### 生成器generator
* 生成器指的是生成器对象，可以由生成器表达式得到，也可以使用**yield**关键字得到一个生成器函数，调用这个函数得到一个生成器对象
* 生成器对象，是一个可迭代对象，是一个迭代器
* 生成器对象，是延迟计算、惰性求值
### yield关键字
* yield关键字，可以中断当前函数执行。如果函数中使用了yield 那么该函数一定是一个生成器函数
### 生成器函数
* 定义：函数体中包含了**yield**关键字的函数，被称作为生成器函数。生成器函数调用后返回生成器对象。生成器函数体**不会**在生成器函数调用时立即执行
* next(generator)可以获取生成器函数生成的**生成器对象**的下一个值
* generator.send(arg)可以获取生成器函数生成的**生成器对象**的下一个值。同时，会将arg的值传递给需要获取yield返回值的对象。
    1. 简单示例一：
    ````python
    def getNum():
    for i in range(5):
        yield i   #注意当执行时遇到yield语句，就暂停该函数的执行。并将yield后面的值返回。
    gnum = getNum() #生成器函数执行，会返回生成器对象。可迭代。

    for i in range(6):
        print(next(gnum)) # 注意，如果函数体执行完成，生成器的游标走到了末尾。会报StopIteration错误
    ````  
    ![yield001](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/yield001.jpg)  
    2. 简单示例二(练习使用send与yield结合)：
    ````python
    def counter():
    def sol():
        n = 0
        while True:
            n += 1
            response = yield n  #使用response获取关键字yield的返回值。注意使用next()调用时返回值是None
            if isinstance(response,int):
                n = response
        soll = sol()  #定义一个sol生成器对象
        return lambda x=None: next(soll) if x is None else soll.send(x)

    cunt = counter() #执行counter函数，获取一个操作计数器的函数。
    print([cunt() for _ in range(5)])  #根据计数器函数获取5个值放在list中
    print(cunt(100))  #初始化计数器函数的初始值
    print([cunt() for _ in range(5)])  #根据计数器函数，获取5个值放在list中
    ````  
    ![yield002](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/yield002.jpg)  

* 注意：
1. 生成器函数中，可以多次使用yield,每次执行一个车yield会暂停执行，把yield表达式的值返回
2. 再次执行会执行到下一个 yield语句，又会暂停
3. return语句依然可以终止函数运行，但return语句的返回值不能被获取到
4. return会结束生成器函数。如果函数体执行完成，生成器的游标就走到了末尾。无法取下一个值，会报StopIteration错误
5. 如果函数没有显式的return语句，生成器函数执行到结尾（相当于执行了return None）,一样会抛出StopIteration异常

* 总结
1. 包含yield语句的生成器函数调用后，会生成**生成器函数**对象。**生成器函数的函数体不会立即执行**
2. next(generator)会从函数的当前位置向后执行到之后碰到的第一个yield语句，会弹出yield语句后面的值。并暂停函数执行。
3. 再次调用next函数，会再次执行函数，如果再次碰到yield，会再次暂停函数，并返回值。如果没有碰到yield而碰到了函数的return语句，会抛出topIteration异常

### 协程Coroutine
* 生成器的高级用法。它比进程、线程轻量级，是在用户控件调度函数的一种实现
* Python3 asyncio就是协程实现，已经加入到标准库
* Python3.5 使用async、await关键字直接原生支持携程
* 协程调度器实现思路  
    * 有两个生成器A、B。next(A)后，A执行到yield语句暂停，然后去执行next(B),B执行到yield语句后也暂停，然后再次调用next(A),再调用next(B)，周而复始，就实现了调度的效果。
    * 可以引入调度的策略来实现切换的方式
* 协程是一种非抢占调度

### yield from语法
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
