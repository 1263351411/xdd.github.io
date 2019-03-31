* Python3引入两个新类型
    * bytes：不可变的字节序列
    * bytearray:可变的字节数组
1. 字符与byts的区别：
    * 字符串是字符组成的有序序列，字符可以使用编码来理解
    * bytes是字节组成的有序的不可变序列
    * bytearray是字节组成的有序的可变序列
2. 编码与解码  
    编码：就是，你用几个字节去理解内存中的数字。  
    解码：就是，你用几个字节去解释字符存放到内存中。
    * 字符串按照不同的字符集编码encode返回字节序列bytes  
        * encode（encoding='utf-8',errors='strict'）->bytes
    * 字节序列按照不同的字符集解码decode返回字符串
        * bytes.decode(encoding='utf-8',errors="strict") -->str 
        * bytearray.decode(encoding="utf-8",errors="strict")-->str    
常用ASCII数字对应的字符：  
【\t】-->9   
【\n】-->10  
【\r】-->13  
[0-9]-->[48-57]   在ASCII表中1对应的16进制表示法是31  
[A-Z]-->[65-90]   在ASCII表中A对应的16进制表示法是41
[a-z]-->[97-122]  在ASCII表中a对应的16进制表示法是61
### ASCII表
![Ascii表](..\img\ASCII表.jpg)
### bytes
1. bytes定义  【注意一个字节是8位，而bytes是字节数组】
    * bytes() #定义一个空的bytes
    * bytes(int) #指定字节的bytes,被0填充 
        * 例如：bytes(15)表示定义一个长度为15的字节组成的数组
    * bytes(iterable_of_ints) -->bytes[0,255]的int组成的可迭代对象  
    * bytes(string,encoding[,errors])-->bytes等价于string.encode()
    * bytes(bytes_or_buffer)-->immutable copy of bytes_or_buffer从一个字节序列或者buffer复制出一个新的不可变的bytes对象
    * 使用b前缀定义：
        * 例如：var = b"abc9"【只允许使用基本的ASCII使用字符形式定义】或者 var = b"\x41\x61"【使用16精制表示】 
2. bytes的操作  
    大部分方法和str类似，都是不可变类型，所以方法很多都一样。只不过bytes方法，输入的是bytes输出的也是bytes  
例如：  
    * replace(bytes,bytes) 替换字符
        * b'abcdef'.replace(b'f',b'k')将字节【abcdef】中的【f】替换成【k】 
    * find(bytes) 寻找指定字符，找到返回对应索引，找不到返回-1
        例如：  
        ![find示例](..\img\bytes01.jpg)   
    * decode()  #将字节序列转换成字符序列
    * 类方法 bytes.fromhex(string)  #默认是两个字符表示一个16进制的数字转换成一个字符  
        * 注意：stirng必须是两个字符的16进制的形式，字符串中的空格将会被忽略
        * bytes.fromhex("6a6b 5d6d")将16进制的数字转换成对应的二进制字符
        * 相关方法：hex() 返回16进制表示的字符串。例如：'abc'.encode().hex()
    * 索引
        b'abcdef'[2]返回该字节对应的数，int类型  
3. int和bytes  
    * int.from_bytes(bytes,byteorder) #将一个字节数组表示成整数。  
        * bytes为字节
        * byteorder 为：【'big'】或者【little】
### bytearray 【可变的字节数组】
* 定义
    * bytearray()  #定义一个空的bytearray
    * bytearray(int)    #定义一个指定长度的bytearray的字节数组，默认被0填充
    * bytearray(iterable_of_ints)   #根据[0,255]的int组成的可迭代对象创建bytearray
    * bytearray(string,encoding[,errors])-->bytearray  #根据string类型创建bytearray，和string.encode()类似，不过返回的是可变对象
    * bytearray(bytes_or_buffe)从一个字节序列或者buffer复制出一个新的可变bytearray对象
* bytearray操作
    * append(int) 尾部追加一个元素
    * insert(index,int)在指定索引位置插入元素
    * extend(iterable_of_ints)将一个可迭代的整数结婚追加到当前bytearray
    * pop(index = -1)从指定索引上移除元素，默认从尾部移除
    * remove(value) 找到第一个value移除，找不到抛异常  
    注意：上述方法若需要使用int类型，值要在[0,255]
    * clear()清空bytearray
    * reverse()翻转bytearray,就地修改
* 示例
示例：
````python
a = 'abcd'.encode()  #将abc字符串解码成字节数组
b = int.from_bytes(a,'big')  #查看变量a字节数组的 高字节编码(将字节数组按照高字节编码转换)
d = int.from_bytes(a,'little') #查看变量a字节数组的，低字节编码（将字节数组按照低字节编码转换）
b1 = b.to_bytes(4,'big')  #将字节按照每4个字节为一个字符转换成对应的字符。字节为高字节编码
b2 = b.to_bytes(4,'little') 
d1 = d.to_bytes(4,'little')
d2 = d.to_bytes(4,'big')
a1 = a.decode()  #将变量a的字节数组编码成对应的字符串
print(a,b,d,a1,d,type(b),b1,b2,d1,d2)
````
![bytes](..\img\bytes02.jpg)
