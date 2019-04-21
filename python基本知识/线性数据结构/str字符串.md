## str字符串
#### 特点：  	
1. 字符串是有序的字符集合  
2. 使用单引号【’】、双引号【”】、三引号【”””或者’’’】 
3. 字符串是不可不变对象  
4. Python3.0起，字符串就是Unicode类型（utf8）  
#### 声明方法
````python
str1 = 'string'
str2 = "string2"
str3 = '''this's a "string" '''
str4 = """select * from user where name = 'xdd' """
````  
![str0001](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0001.png)  
##### 配合字符串使用的符号
* 【\n】换行符号
* 【\t】相当于TAB按键
* 【r”” 或者R””】表示不转译字符串中特殊符号
    * 例如：str5 = r”hello \n xdd”	  
    ![str0002](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0002.png) 
* 常用转译字符有  
 ![str0003](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0003.png) 
 ##### 常用方法
 * join(iterable)->str 将可迭代对象使用指定字符【string】链接成新的字符返回。（注意：可迭代对象本身就是字符串）  
    * iterable为可迭代对象  
    ![str0037](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0037.png)
 * replace(old,new[,count])->str #将字符中匹配到old的字符串替换成new新的字符串
    * old 需要替换的字符
    * new 替换字符
    * count 替换次数，不指定默认全部替换  
     ![str0014](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0014.png)
* strip([chars])->str #将自定字符串两端去除自定的字符集chars中的所有字符,如果chars没有指定，去除两端的空白字符
    * chars 切割符  
    ![str0016](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0016.png)  
    ![str0017](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0017.png)  
##### 查找字符
* find(sub[,start[,end]])->int #在指定区间[ start,end),从左至右，查找字符串sub。找到返回索引，没找到返回-1
    * sub 要查找的字符串
    * start查找起始点索引
    * end查找区间的结束索引（不包含结束索引）  
    ![str0018](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0018.png)  
* rfind(sub[,start[,end]])->int #在指定区间[start,end)从右到左，查找字符串sub,找到返回索引，没找到返回-1
    * sub 要查找的字符串
    * start 要查找的起始点索引
    * end 要查找区间的结束索引（不包含结束索引）  
    ![str0019](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0019.png)  
* index(sub[,start[,end]])->int #在指定的区间[start,end)，从左到右，查找子串sub。找到返回索引，没找到抛出异常ValueError（如果不设置start和end就在整个字符串中查找）
	* sub 要查找的字符串
	* start 查找区间的起始索引
	* end 查找区间的结束索引（不包含结束索引）  
    ![str0020](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0020.png)   
* rindex(sub[,start[,end]])->int #在指定的区间[start,end)，从右到左，查找子串sub。找到返回索引，没找到抛出异常ValueError（如果不设置start和end就在整个字符串中查找）
	* sub 要查找的字符串
	* start 查找区间的起始索引
	* end 查找区间的结束索引（不包含结束索引）  
##### 统计判断
* count(sub[,start[,end]])->int #在制定区间[start,end),从左到右，统计子串sub出现的次数（如果没有自定start和end默认在整个字符串中统计） 
	* sub 要统计的字符串
	* start 统计的起始索引
	* end 统计的结束索引（不包含结束索引）  
    ![str0021](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0021.png)   
* endswith(suffix[,start[,end]])->bool #在指定区间[start,end),字符串是否是suffix字符结尾，是返回True 否返回False。如果不指定区间，默认区间是整个字符串   
    ![str0022](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0022.png)  
* startswith(prefix[,start[,end]])->bool #在指定区间[start,end)，字符串是否是prefix开头。如果不指定区间，默认区间是整个字符串  
    ![str0023](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0023.png)  
* isalnum()->bool 是否是字母和数字组成
* isalpha()->bool 是否是字母
* isdecimal()->bool 是否只包含十进制数字
* isdigit()->bool	是否全部数字（0-9）
* isidentifier()->bool 是否是字母下划线开头，其他都是字母、数字、下划线
* islower()->bool 是否都是小写
* isupper()->bool 是否都是大写
* isspace()->bool 是否只包含空白字符

 ##### 切割字符类
 * split(sep=None,maxsplit=-1) -> str类型的list集合，使用自定义字符来切割字符串
    * 使用自定的字符切割字符串，返回切割后的字符数组
    * sep指定分割字符串，缺省情况下空白符号为切割符号。
    * maxsplit 指定切割的次数，-1表示遍历整个字符串      
     ![str0004](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0004.png)    
     ![str0005](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0005.png)   
* splitlines(keepends)->str类型的list集合，使用行来切割字符串
    * 使用行来切割字符，行分隔符包括【\n】【\r\n】【\r】等
	* keepends指是否保留行分隔符，默认不保留（默认值：keepends=False）   
    ![str0006](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0006.png) 
* partition(sep)->(head,sep,tail) 切割字符串，返回一个三元组。(从左到右切割)
    * sep切割符号，必须指定
    * 将指定字符从左至右切割成，头部，分割符，尾部三部分组成的三元组；如果没有找到分割符，就只返回头部和2个空元素的三元组。  
    ![str0007](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0007.png) 
* rpartition(sep)->(head,sep,tail) 切割字符串，返回一个三元组（从右到左切割）
    * 将指定字符从右到左切割成，头部，分隔符，尾部三部分组成的三元组；如果没有找到分隔符，就返回2个空元素和尾的三元组  
    ![str0008](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0008.png)   
##### 大小写转换类
* upper()->str  #将字符中所有字符转换成大写
* lower()->str  #将字符中所有字符转换成小写
* swapcase()->str #将字符中大写转换成小写，小写转换成大写
* capitalize()->str #将字符串中首个单词的首字母转换成大写字母  
![str0009](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0009.png)   
* title()->str  #将英文单词中每个字母的首字母都转换成大写字母  
![str0010](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0010.png)    
##### 位置调整类
* center(width[,fillchar])->str #将字符串按照指定方宽度居中显示。空白位置使用fillchar填充。默认值为空格符号
    * width 总宽度
    * fillchar 填充的字符(不能是字符串)  
    ![str0011](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0011.png) 
* zfill(width)->str #将指定字符按照width宽度居右显示。不够的地方使用0填充
    * width:打印宽度，局右，左边用0填充  
    ![str0012](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0012.png)   
* ljust(width[.fillchar])->str #将字符左对齐显示width长度，不够长度使用fillchar字节替代。
    * width:打印宽度
    * fillchar: 补充字符
    ![str0013](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0013.png)  
* rjust(width[,fillchar])->str #将字符右对齐显示width长度，不够使用fillchar字节替代。  
![str0015](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0015.png)  
###  字符串的格式化
##### C语言风格的字符串格式  
* 在2.5版本之前，只能使用printf style风格的print输出  
	* printf-style formatting,来自于C语言的printf函数
* 格式要求：
    1. 占位符：使用%和格式字符组成。例如%s 、%d等
        * s调用star()，r会调用repr()。所有对象都可以被这两个转换。
    2. 站位富中还可以插入修饰字符，例如%03d表示打印字符的位置长度为3，不够签名补0
    3. format % values，格式字符串和被格式的值之间使用%分隔
    4. values只能是一个对象；或者一个和格式字符串占位符数目相等的元组，或一个字典
![str0024](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0024.jpg) 
* 例子No1 
	* 【"%d get me %f" % (20,20.222)】输出结果为：'20 get me 20.222000'
* 例子No2
    * 【"I an %03d" % 20】也等价于【”I am %03d” % (20,)】
其中：%03d 输出一个整数，这个整数有效位数小于3时，在数字前面补0  
![str0025](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0025.png)   
* 例子No3
    * 【"I like %s" % 'Python'】   
    ![str0026](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0026.png)   
* 例子No4
    * 【"%3.2f%%,0x%x,0x%02X" % (65.5687,10,16)】
    * 其中：
        * 【%3.2f%%】表示，输出一个浮点数，
        * 【整数部分+小数点+小数部分】有效位数一共为3位，其中小数部分有效位数为2位。不够的位数用空格补齐。其中%%为转译输出%号。如果是【%03.2f%%】那么不够的位数就用0补齐
        * 【0x%x】按照16进制输出 10 在16进制数中对应a  
        ![str0027](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0027.png)   
* 例子No5
    * 【"%0-10.2f%%,0x%x,0x%02X" % (65.5687,10,16)】
	* 其中【%0-10.2f%%】中【-】负号表示右对齐，默认不写为左对齐  
    ![str0028](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0028.png)   
##### format字符串格式化
* 语法：”{}{xxx}”.format(*args,**kwargs)->str
    * args是位置参数，是一个元组
	* kwargs是关键字参数，是一个字典
	* {}花括号为占位符，表示按照顺序匹配参数，{n}表示取位置参数args[n]对应的值
	* {xxx}其中xxx为关键字名称，表示在关键字参数kwargs中搜索名称一致的参数对应值
	* {{}}表示打印花括号（注意：双符号表示转译输出）
* 位置参数：
    * 按照位置顺序用位置参数替换前面的格式字符串的占位符
    * 例如：【“{}:{}”.format(“192.168.61.100”,8888)】  
    ![str0029](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0029.png)   
* 关键字参数或命名参数
    * 位置参数按照序号匹配，关键字参数按照名称匹配 
    * 例如：【{server}{1}:{0}.format(8888,”192.168.61.100”,server=”xdd”)】  
    ![str0030](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0030.png)    
* 访问元素： 
    * 例如：【"{0[0]}.{0[1]}".format(('xdd','com'))】  
    ![str0031](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0030.png)  
* 对象属性访问  
    * 例如：【"({p1.x},{p1.y})".format(p1=p)】  
    ![str0032](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0032.png) 
* 对齐
    * 例如：【"{0}\*{1}={2:<3}".format(3,2,3*2)】 
    * 其中【{2:<3}】表示输出数组中下标为2的内容。输出字符长度为3个字符长度，如果不够用空格补齐。<小于号表示向左对齐输出 
    ![str0033](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0033.png)  
* 居中
    * 例如：【{:*^30}.format(‘centered’)】 
        * 表示将centerd单词居中显示，显示长度为30个字符，不够的地方用*星号替代
        * 【^】表示居中  
    ![str0034](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0034.png)   
* 进制
    * 例如：【"int:{0:d}; hex:{0:x}; oct:{0:o}; bin:{0:b}".format(50)】
        * 其中【{0:d}】表示按照十进制数字输出
	    * 【{0:x}】表示按照十六进制数字输出
	    * 【{0:o}】表示按照八进制数字输出
	    * 【{0:b}】表示按照二进制数字输出
	    * 【{0:#b}】中#表示输出数字时，带上精制数的对应表示符号  
     ![str0035](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0035.png)    
    * 例如：![str0036](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/str0036.png)    
        * 其中：192.168.0.1名称：点分四段十进制表示法的ipv4地址
        * 【.format(\*octets)】中\*表示，将octets列表转换为对应长度的元素

    




    






