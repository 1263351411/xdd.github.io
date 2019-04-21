## list列表 
* 一个队列，一个排列整齐的队伍
* 列表内的个体称作元素，list列表是由若干个元素组成列表
* 元素可以是任意对象（数字、字符串、对象、列表等）
* 列表内元素有顺序，可以使用索引
* 列表是线性数据结构
* 列表是可变的使用[]表示
#### 列表的定义（初始化）
````python
lst  = list()  #定义了一个空列表，名称叫做lst
lst2 = []   #定义了一个空列表，名称叫做lst2
lst3 = [1,2,3,'ab'] #定义了一个列表
lst4 = list(range(5)) #使用可迭代对象定义了一个列表
````
* 注意：列表的长度是可变的

#### 列表的索引访问
* 索引,也叫下标，分为正索引，负索引
    * 正索引：从左至右，从0开始，为列表中每一个元素编号
    * 负索引：从右到左，从-1开始，
    * 正负索引都不可越界，否则引发异常IndexError
* 列表可以通过索引访问。
    * list[index] ,index就是索引，使用中括号访问
    ````python
    lst = [1,2,3,4]
    print(lst,lst[1],sep="\n")
    ````
    * 输出如下：  
    ![list001](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/list001.jpg)  
#### 列表中的常用方法
###### 查询
* index(value[,start[,stop]])->int #通过value值，从指定区间查找列表内的元素是否匹配，匹配第一个就立即返回其对应索引，匹配不到，抛出异常ValueError
    * value 需要查找的值
    * start 查找范围的起始索引
    * stop 查找范围的结束索引
    * int 返回值时int类型，即值对应的索引
    * 注意：如果不指定start,stop默认从左到右全局看查找，找到第一个就返回其对应索引，找不到，抛出异常ValueError 
    * 查找的时间复杂度是O(n)，最坏需要遍历整个列表
* count(value)->int #返回列表中匹配value的次数
    * value 需要匹配的值
    * int 在列表中value出现的次数
    * 查找的时间复杂度是O(n),需要遍历整个列表
* len(list)->int 返回list列表中元素的个数。时间复杂度O(1)
##### 元素的修改
* list[index] = value #将列表中索引为index的值修改为value,注意index索引不能超界
##### 添加元素
* append(object)->None 在列表尾部追加元素object，返回值None。就地修改，时间复杂度O(1)
    * object需要插入的元素
* insert(index,object)->None 在指定索引index处插入元素object,返回值None。就地修改。时间复杂度O(n)
    * index 插入元素的所有位置
    * object需要插入的元素
    * 注意index可以越界。
        * **超过上边界，在首部添加**。这样会导致整个列表list中所有元素位置都向后挪动，此时时间复杂度最大为O(n).
        * **超过下边界，在尾部追加**。此时相当于append方法，直接在尾部追加，时间复杂度为O(1)
* extend(iterable)->None 将可迭代对象的元素追加到尾部，返回值None.就地修改
* + -> list 将两个列表链接起来，产生一个新的列表，原列表不变。本质上是调用了__add()__方法
````python
[1,2,3] + [4,5,6]  # 会返回一个新列表[1,2,3,4,5,6]
````  
* * ->list 重复操作，将本列表元素重复n次，返回新的列表
````python
[0]*5  #会返回一个新列表[0,0,0,0,0]
[[1,2]]*3 #会返回一个新列表[[1,2],[1,2],[1,2]]注意，次数列表中的3个元素都是应用类型，都指向同一个列表[1,2]如果，列表[1,2]的元素被修改，其他3个列表中的元素也同样会被修改。
````  
##### 删除元素
* remove(value)->None 从左至右查找第一个匹配value的值，移除该元素，返回None.就地修改。效率比较低,会产生元素的挪动。
* pop([index])->obj #删除指定索引index位置的元素，如果不指定，默认从列表尾部删除。返回被删除元素的对象。
    * index 需要删除元素所在位置的索引。如果不是从尾部删除，会产生元素的挪动。时间复杂度最大为O(n),如果从尾部删除，时间复杂度为O(1)
* clear()->None 清除列表索引元素，剩下一个空列表，就地修改。
##### 其他操作
* reverse()->None 将列表元素反转，返回None。就地修改
* sort(key=None,reverse=False)->None 对列表元素进行排序，就地修改，默认升序
    * key 一个函数，指定key如何排序 lst.sort(key=function)
    * reverse反转，默认值为False,表示升序，如果指定reverse=True,表示降序
* in 判断一个元素是否在列表里面
````python
[3,4] in [1,2,[3,4]] #判断列表[3,4]是否在列表[1,2,[3,4]]里面。这里返回值时True
for x in [1,2,3,4] #用在for循环里面，可以遍历整个列表中的元素。
````
##### 列表复制
* copy()->list 会返回一个新列表。注意copy是浅拷贝，如果列表中的值有引用类型，只会复制引用类型的地址。
    * 如果想使用影子拷贝，也叫深拷贝。深拷贝遇到引用类型，会在内存中重新创建一个和引用类型所指向的对象。
    * copy模块提供了deepcopy方法可以达到深拷贝
    ````python
    import copy
    lst1 = [0,1,2,[3,4,5]]
    lst2 = lst1.copy() #浅拷贝
    lst3 = copy.deepcopy(lst1) #对lst1进行深拷贝
    ````
    * 浅拷贝模型图   
    ![list002](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/list002.jpg)   

##### 注意：
````python
lst0 = list(range(5))
lst1 = list(range(5))
print(lst0==lst1) #会打印True,因为==默认会比较列表中元素的值。
````
    

