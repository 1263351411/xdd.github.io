## 字典dict  
* 字典是一个非线性结构，是key-value组成的键值对的数据集合。
* 字典的特点：可变的、无序的、key不重复。  
## 字典的定义
* 【{}或者dict()】可以定义一个空字典
    * 例如：
    ````python
    a = dict()
    b = {}
    print(a,b,type(a),type(b))
    ````  
    ![dict001](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/dict001.jpg)
* 【dict(**kwargs)】可以使用name=value键值对，初始化一个字典
    * 例如：  
    ````python
    c = dict(gdy="abc",x=90,y=100)
    print(c,type(c))
    ````  
    ![dict002](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/dict002.jpg)
* 【dict(iterable,**kwarg)】使用可迭代对象和name = value度构造字典、不过可迭代对象的元素必须是一个二元结构  
    * 例如：
    ````python
    d = dict((("a","001"),("b","002")))
    print(d,type(d))
    ````  
    ![dict003](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/dict003.jpg)
* 【dict(mapping,**kwarg)】使用一个字典构建另一个字典
    * 例如：
    ````python
    e = {"a":10,"b":20,"c":30}
    f = dict(e,abc="20")
    print(e,f)
    ````  
    ![dict004](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/dict004.jpg)
* 【{}】直接定义：例如：e = {"a":10,"b":20,"c":30}  
* fromkeys(iterable,value) 【类方法】 #根据建集合初始化一个字典
    * iterable ：为可迭代的键值集合
    * value：为默认所有建对应的默认值。(可以不写，如果没有默认为None)
    * 例如：
    ````python
    a = dict.fromkeys(range(10),0)
    b = dict.fromkeys(range(10))
    print(a)
    print(b)
    ````  
    ![dict005](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/dict005.jpg)  

## 字典元素的访问  
* 【d[key]】 返回可用对应的值value,如果可以不存在会抛出keyError异常
* 【get(key[,default])】 返回key对应的值value，如果key不存在就返回缺省值default，缺失值默认为None
* 【setdefault(key[,default])】返回key对应的值value,如果key不存在，添加kv对，value设置为default,并返回default，如果default没有设置，则返回None  
* 【keys()】获取字典中所有key的集合
* 【values()】或者字典中所有值values的集合
* 【items()】获取字典中所有键值对组成的集合
## 字典增加和修改
* 【d[key] = value】将key对象的值修改为value,*如果key不存在就添加新的key对应value*
* 【update([other])--->None】 使用一个字典里面的数据对本字典的更新，如果key不存在就添加，key存在就覆盖已经存在的key对应的值。 就地修改，无返回值
    * 例如：
    ````python
    a = {"1":10,"2":100,"3":200,"b":10,"c":20}
    print(a)
    a.update(b=100) #更新键值为b的值为100
    print(a)
    a.update([("1","ab")]) #将键值"1"的值修改为"ab"
    print(a)
    c = a.setdefault(1,5)  #获取键值为1对应的value的值，如果没有就插入键值对1,5 ,并返回默认值
    c2 = a.setdefault(1,6) #获取键值为1对应的value的值，如果没有就插入键值对1,6，滨返回默认值
    print(a,c,c2)
    a.update([(1,2)])  #将键值对key=1的值修改为2，如果没有找到键值为1,就添加键值对1,2
    print(a)
    a.update([(1,5)])  #将键值为1对应的值修改为5
    print(a)
    ````  
    ![dict006](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/dict006.jpg)  
## 字典的删除
* 【pop(key[,default])】 将key对应的值删除，并返回key对应的值。如果key不存在就返回缺省值defalut。如果未设置default，并且key不存在会抛出异常keyError
* 【popitem()】移除并返回任意的键值对，字典为empty空时会抛出异常KeyError
* 【clear()】清空字典
* 相关参数 del语句
    * 例如【del a['c']】看着像删除了一个对象，本质上减少了一个对象的引用，del实际上删除的是名称，而不是对象。
    ````python
    a = True
    b = [1,2]
    c = [b,3]
    print(a,b,c)
    del a  #将变量a的名称删除
    #print(a)  #会报错，因为变量a已经不存在
    del b  #将变量b的名称删除
    print(c)
    ````  
    ![dict007](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/dict007.jpg)  
## 字典的遍历
* list(d.keys()) 根据字典的建集合或对应的list集合
    注意：【for i in a.keys() 】等价于【for i in a】或者直接使用如下方法直接遍历出元素和元组
    【for i,k in a.items()】
    * 例如： 
    ````python
    a = dict(a=1,b=2,c=3,d=4,e=5)
    print(a.keys())
    b = list(a.keys())
    print(b)
    for i in a.keys(): print(i)   #打印所有key的值
    print("-----------------")
    for k in a : print(k)  
    ````  
    ![dict008](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/dict008.jpg)   
## 总结
* python3中 keys、values、items方法返回一个类似生成器的可迭代对象，不会吧函数的返回结果复制到内存中，返回的对象可以使用len()、iter()、in操作
## 相关字典
#### 缺省字典（defaultdict）
* 需要导入模块import collections
* 定义方式：
````python
import collections
defdict = collections.defaultdict(dict) #建立一个缺省值为dict的缺省字典。
deflist = collections.defaultdict(list) #建立一个缺省值为list的缺省字典。
defset = collections.defaultdict(set)  #建立一个缺省值为set的缺省字典。
defdict["c"] = 1
defdict.update([("a","b")])
deflist["a"] = 1
defset["b"] = 1
for i in range(5):
    deflist[i].append(i) #当key=i的键对应的值不存在是，默认创建一个key对应的list集合。并在集合中添加i元素
    defset[i].update([(i,i)]) #当key=i的键对应的值不存在是，默认创建一个key对应的set集合。并在集合中添加i元素
    defdict[i].update([(i,i)]) #当key=i的键对应的值不存在是，默认创建一个key对应的dict集合。并在集合中添加i元素
print(defdict,deflist,defset,sep="\n")
````  
![dict009](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/dict009.jpg)  
#### 有序字典（OrderedDict）
* 和defaultdict一样，需要导入模块import collection
* 定义方式和defaultdict类似。但不同的是OrderedDict是有序字典，里面元素的排列顺序是元素的插入顺序。
    * 注意：3.6版本中的Python的字典就是记录key插入的顺序（IPython不一定有效）
* 简单示例
````python
import collections
order = collections.OrderedDict() #实例化一个有序字典
order.update([(4,10)]) # 插入键值对4,10
for i in range(5):   #给字典插入新元素
        order[i] = i
order.setdefault(6,10)  #给字典插入新元素
print(order.keys())
print(order.values())
print(order)
````  
![dict010](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/dict010.jpg)  
* 有序字典排序
    * sorted(iterable, /, *, key=None, reverse=False) 函数会返回一个新的字典对象
    * 例如：
    ````python
    import random,string
    word = { _:2 for _ in [random.choice(string.ascii_lowercase) for _ in range(20)]}  #随机生成20个字母组成的字典
    print(word)
    wordsort = sorted(word.items())  #使用sorted将字典，按照key排序。
    print(wordsort)
    ````  

    ![dict011](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/dict011.jpg)  

#### 字典与list结合使用：
* 可以使用字典记录元素。在加个列表list记录存在字典中元素的实际位置，用列表的顺序记录在字典中对应元素的大小。这样在使用list遍历时，可以保证在列表中元素的顺序。而再查找元素时使用字典查找，保证了检索的速度，避免了list的缺点。
