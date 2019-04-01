* Python3引入两个新类型
    * bytes：不可变的字节序列
    * bytearray:可变的字节数组
1. 字符与byts的区别：
    * 字符串是字符组成的有序序列，字符可以使用编码来理解
    * bytes是字节组成的有序的不可变序列
    * bytearray是字节组成的有序的可变序列
2. 编码与解码  
    编码：就是，你用几个字节去理解内存中的数字。  
    解码：就是，将内存中的字节数组按照什么字符集解码成对应的字符
    * 字符串按照不同的字符集编码encode返回字节序列bytes  
        * encode（encoding='utf-8',errors='strict'）->bytes
            * 注意encode默认转换时的默认编码集是utf-8
    * 字节序列按照不同的字符集解码decode返回字符串
        * bytes.decode(encoding='utf-8',errors="strict") -->str 
        * bytearray.decode(encoding="utf-8",errors="strict")-->str  
            * 注意：decode方法默认解码时，默认的编码集是utf-8   
    * 示例 1：
        ````python
        a = 'abc'
        c = a.encode()  #将abc字符串编码成字节数组
        d = c.decode()  #将变量c的字节数组解码成对应的字符串
        print(a,c,d,sep="\t")
        ````
        ![encode and decode](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/bytes02.jpg) 
    * 示例 2：  encode()指定编码集
        ````python
        a = '你好'
        a1 = a.encode(encoding="utf-8") # 用utf-8编码集将字符串a转换成对应的字节数组
        a2 = a.encode(encoding="gbk")  # 用gbk编码集将字符串a转换成对应的字节数组
        a11 = a1.decode(encoding = "utf-8") #用utf-8编码集将字节序列a1转换成对应的字符（注意编码时和解码时的编码集要保持一致，不然会出现如下a12乱码）
        a12 = a1.decode(encoding = "gbk")
        print("a = {}\na1 = {}\na2 = {}\na11 = {}\na12 = {}".format(a,a1,a2,a11,a12))
        ````
        ![encode and decode for encoding](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/bytes05.jpg)   

* 常用ASCII数字对应的字符：  
    * 【\t】-->9   
    * 【\n】-->10  
    * 【\r】-->13  
    * [0-9]-->[48-57]   在ASCII表中1对应的16进制表示法是31  
    * [A-Z]-->[65-90]   在ASCII表中A对应的16进制表示法是41
    * [a-z]-->[97-122]  在ASCII表中a对应的16进制表示法是61
### ASCII表
![Ascii表](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/ASCII表.jpg)
### bytes
1. bytes定义  【注意一个字节是8位，而bytes是字节数组】
    * bytes() #定义一个空的bytes
    * bytes(int) #指定字节的bytes,被\x00填充 
        * 例如：bytes(15)表示定义一个长度为15的字节组成的数组
    * bytes(iterable_of_ints) -->bytes[0,255]的int组成的可迭代对象  
        * 例如：  
        ````python
        arr = [61,62,63]
        arr2 = bytes(arr)  # 根据int类型列表转换成对应的字节列表,注意列表中int类型的值取值范围是【0-255】
        arr3 = list(arr2) # 根据字节列表，将每个字符转换成对应的十进制数存放在新的list列表里面
        arr4 = arr2.hex() #将字节列表，转换成对应的16进制字符串
        print("arr = {}\narr2 = {}\narr3 = {}\narr4 = {}".format(arr,arr2,arr3,arr4))
        ````    
        ![byts示例](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/bytes03.jpg) 

    * bytes(string,encoding[,errors])-->bytes等价于string.encode(),将string字符集按照指定的编码表解码成对应的bytes集合。
    * bytes(bytes_or_buffer)-->immutable copy of bytes_or_buffer从一个字节序列或者buffer复制出一个新的不可变的bytes对象  
        * 注意：当copy的序列中是python的常量时，在python底层不会真的去拷贝一份常量，只是增加常量的引用次数.因为bytes字节数组是不可变的。
        * 例如：
            ````python
            s = "年第三".encode()
            s1 = bytes(s)
            print(s,s1)
            print(id(s),id(s1))
            ````  

            ![find示例](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/bytes10.jpg)    
    
    * 使用b前缀定义：
        * 例如：var = b"abc9"【只允许使用基本的ASCII使用字符形式定义】或者 var = b"\x41\x61"【使用16精制表示】 
2. bytes的操作  
    大部分方法和str类似，都是不可变类型，所以方法很多都一样。只不过bytes方法，输入的是bytes输出的也是bytes  
例如：  
    * replace(bytes,bytes) 替换字符
        * b'abcdef'.replace(b'f',b'k')将字节【abcdef】中的【f】替换成【k】 
    * find(bytes) 寻找指定字符，找到返回对应索引，找不到返回-1
        * 例如：  
        ![find示例](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/bytes01.jpg)   
    * decode()  #将字节序列转换成字符序列
    * bytes.fromhex(string)  类方法 #默认是两个字符表示一个16进制的数字转换成一个字符 
        * 注意：stirng必须是两个字符的16进制的形式，字符串中的空格将会被忽略
        * bytes.fromhex("6a6b 5d6d")将16进制的数字转换成对应的二进制字符
        * 相关方法：hex() 返回16进制表示的字符串。例如：'abc'.encode().hex() 
        * 示例
        ````python
        num = "61 6263"
        num1 = bytes.fromhex(num) #将16进制的数字转换成对应的字节
        num2 = num1.hex() #将字节转换成对应的16进制字符串
        num3 = list(num1) #将字节转换成对应的10进制数，存放在新列表中
        print("num1 = {}\n num2 = {} \n num3 = {}".format(num1,num2,num3))
        ````  
        ![find示例](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/bytes04.jpg)  
    * 索引
        b'abcdef'[2]返回该字节对应的数，int类型  
### bytearray 【可变的字节数组】
* 定义
    * bytearray()  #定义一个空的bytearray
    * bytearray(int)    #定义一个指定长度的bytearray的字节数组，默认被\x00填充
    * bytearray(iterable_of_ints)   #根据[0,255]的int组成的可迭代对象创建bytearray
    * bytearray(string,encoding[,errors])-->bytearray  #根据string类型创建bytearray，和string.encode()类似，不过返回的是可变对象
    * bytearray(bytes_or_buffe)从一个字节序列或者buffer复制出一个新的可变bytearray对象,和bytes不同，他会复制一个新的对象。
        * 例如：
        ````python
        s = 'abcd'
        s1 = s.encode()  #将字符集按照utf-8编码成字字节数组
        s2 = bytes(s1)  #根据s1字节数组拷贝一个新的字节数组
        s3 = bytearray(s2)
        s4 = bytearray(s3) 
        print(s1,s2,s3,s4,sep = "\t\t")
        print(id(s1),id(s2),id(s3),id(s4),sep = "\t\t")
        ````  

        ![find示例](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/bytes11.jpg)
* bytearray操作
    * append(int) 尾部追加一个元素
    * insert(index,int)在指定索引位置插入元素
    * extend(iterable_of_ints)将一个可迭代的整数结婚追加到当前bytearray
    * pop(index = -1)从指定索引上移除元素，默认从尾部移除
    * remove(value) 找到第一个value移除，找不到抛异常  
    注意：上述方法若需要使用int类型，值要在[0,255]
    * clear()清空bytearray
    * reverse()翻转bytearray,就地修改
### int和bytes  
* int.from_bytes(bytes,byteorder) #将一个字节数组表示成整数。 需要指定模式
    * bytes为字节
    * byteorder 为：【'big'】或者【little】
        * 大端模式(big) :低字节如果放在高地址上。叫大端模式
        * 小端模式(tittle):低字节如果放在低地址上，称为小端模式
* int.to_bytes(length,byteorder) #将一个整数表达成指定长度的字节数组
* 大小端图解  
![find示例](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/bytes06.jpg)   
![find示例](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/bytes07.jpg)  

* 示例1：   
![find示例](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/bytes08.jpg)   
* 示例2： 
````python
a = "abc"
a1 = a.encode()  #将字符abc转出字节数组 默认编码方式是utf-8
a2 = int.from_bytes(a1,"big")  #将字节数组，用int数组表示法，使用大端模式转成int类型
a3 = a2.to_bytes(3,"big")  #将a2转换成字节数组，需要指定int类型的a2表示了几个字节，使用了什么模式
a4 = a3.decode()  #将字节数组解码，默认解码方式是utf-8
print("a = {}\na1 = {}\na2 = {}\na3 = {}\na4 = {}".format(a,a1,a2,a3,a4))
````    

![find示例](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/bytes09.jpg) 
