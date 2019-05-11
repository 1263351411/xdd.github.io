# argparse命令行解析模块
@[toc]
一个可执行文件或者脚本都可以接受参数。
````shell
ls -l /etc
# /etc 是位置参数
# -l 是短选项
# /etc对应的是位置参数 -l对应的是选项参数
```` 
* 参数分类：
    1. 位置参数：参数放在那里，就要对应一个参数位置。  
    2. 选项参数：必须通过前面是\-的短选项或者\-\-长选项，开头的字符串，后面字符才算选项参数，当然选项后面也可以没有参数。  

## argparse模块中的ArgumentParser对象
* argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True)->ArgumentParser对象
    * **prog**  #程序的名字，缺省使用sys.argv[0]的basename
    * **usage** #str类型，描述程序使用情况的字符串。默认值为None，表示由添加到程序使用参数的字符串生成。
    * **description**   #str类型。程序的描述信息
    * **epilog**    #str类型。参数help之后显示的文本信息。
    * **parents**   #list类型。ArgumentParser对象中使用的参数组成的列表。默认值为[]空列表
    * **formatter_class**   #class。自定义帮助输出的类。
    * **prefix_chars**  #前缀参数的字符集合。默认值为"-"
    * **fromfile_prefix_chars** #附加参数的前缀文件的一组字符
    * **argument_default** #参数的全局默认值，默认值为None
    * **confict_handler** #解决冲突选项的策略，通常不需要设置。
    * **add_help**  #是否自动为解析器增加-h和--help选项，默认值为True
    * **allow_abbrev** #允许长选项被缩写 默认值为：True
* 简单示例：
````python
import argparse
parser = argparse.ArgumentParser() #获得一个参数解析器
args = parser.parse_args("") #分析参数 注意：如果是控制台允许可以将参数“”去掉，接受控制台传入
parser.print_help() #打印帮助
````   
执行结果为：   
![argparse001](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/argparse001.jpg)
1. argparse不仅仅帮助做了参数解析，还会自动帮助生成帮助信息。尤其是usage,可以看到现在定义的参数是否是自己想要的。 

## ArgumentParser对象常用方法
* add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])  
    * name or flags # 参数名称 例如-f,--foo
    * action #命令行中遇到此参数后采取的基本操作类型
        * action可选值为如下：都是str类型。
        * "store" #默认操作，表示添加的参数用来存储一个值。
            ````python
            >>> parser = argparse.ArgumentParser()
            >>> parser.add_argument('--foo')
            >>> parser.parse_args('--foo 1'.split())
            Namespace(foo='1')
            ````
        * "store_const" #需要结合const来使用表示参数，如果用户传入了指定的参数，那么参数对应的值九尾const指定的值。
            ````python
            >>> parser = argparse.ArgumentParser()
            >>> parser.add_argument('--foo', action='store_const', const=42)
            >>> parser.parse_args(['--foo'])
            Namespace(foo=42)
            ````
        * "store_true" #用户指定了参数。那么参数对应的值就为True，否则为False
        * "store_false" #用户指定了参数。那么参数对应的值就为False,否则为True
            ````python
            >>> parser = argparse.ArgumentParser()
            >>> parser.add_argument('--foo', action='store_true')
            >>> parser.add_argument('--bar', action='store_false')
            >>> parser.add_argument('--baz', action='store_false')
            >>> parser.parse_args('--foo --bar'.split())
            Namespace(foo=True, bar=False, baz=True)
            ````
        * "append" #用户可以多次为参数设置值，值会存储在一个列表中。
            ````python
            >>> parser = argparse.ArgumentParser()
            >>> parser.add_argument('--foo', action='append')
            >>> parser.parse_args('--foo 1 --foo 2'.split())
            Namespace(foo=['1', '2'])
            ````
        * "append_const" #最佳参数，可以和多个设定的参数联合使用。如果两个参数同时设定，会规整到同一个属性上。
            ````python
            >>> parser = argparse.ArgumentParser()
            >>> parser.add_argument('--str', dest='types', action='append_const', const=str)
            >>> parser.add_argument('--int', dest='types', action='append_const', const=int)
            >>> parser.parse_args('--str --int'.split())
            Namespace(types=[<class 'str'>, <class 'int'>])
            ````
        * "count" #统计关键字参数出现的次数
            ````python
            >>> parser = argparse.ArgumentParser()
            >>> parser.add_argument('--verbose', '-v', action='count')
            >>> parser.parse_args(['-vvv'])
            Namespace(verbose=3)
            ````
        * "version" #在add_argument()中使用，通常用来打印版本信息
            ````python
            >>> import argparse
            >>> parser = argparse.ArgumentParser(prog='PROG')
            >>> parser.add_argument('--version', action='version', version='%(prog)s 2.0')
            >>> parser.parse_args(['--version'])
            PROG 2.0
            ````
    * nargs #这参数接受结果参数
        * N #数字，必输是指定数目个数
            ````python
            >>> parser = argparse.ArgumentParser()
            >>> parser.add_argument('--foo', nargs=2)
            >>> parser.add_argument('bar', nargs=1)
            >>> parser.parse_args('c --foo a b'.split())
            Namespace(bar=['c'], foo=['a', 'b'])
            ````
        * ? #表示可有可无
            ````python
            >>> parser = argparse.ArgumentParser()
            >>> parser.add_argument('--foo', nargs='?', const='c', default='d')
            >>> parser.add_argument('bar', nargs='?', default='d')
            >>> parser.parse_args(['XX', '--foo', 'YY'])
            Namespace(bar='XX', foo='YY')
            >>> parser.parse_args(['XX', '--foo'])
            Namespace(bar='XX', foo='c')
            >>> parser.parse_args([])
            Namespace(bar='d', foo='d')
            ````
            * 还可以配合指定输入输出文件
            ````python
            >>> parser = argparse.ArgumentParser()
            >>> parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
            ...                     default=sys.stdin)
            >>> parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
            ...                     default=sys.stdout)
            >>> parser.parse_args(['input.txt', 'output.txt'])
            Namespace(infile=<_io.TextIOWrapper name='input.txt' encoding='UTF-8'>,
                    outfile=<_io.TextIOWrapper name='output.txt' encoding='UTF-8'>)
            >>> parser.parse_args([])
            Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>,
                    outfile=<_io.TextIOWrapper name='<stdout>' encoding='UTF-8'>)
            ````
        * + #表示至少一个
            ````python
            >>> parser = argparse.ArgumentParser(prog='PROG')
            >>> parser.add_argument('foo', nargs='+')
            >>> parser.parse_args(['a', 'b'])
            Namespace(foo=['a', 'b'])
            >>> parser.parse_args([])
            usage: PROG [-h] foo [foo ...]
            PROG: error: the following arguments are required: foo
            ````
        * * #表示任意个
            ````python
            >>> parser = argparse.ArgumentParser()
            >>> parser.add_argument('--foo', nargs='*')
            >>> parser.add_argument('--bar', nargs='*')
            >>> parser.add_argument('baz', nargs='*')
            >>> parser.parse_args('a b --foo x y --bar 1 2'.split())
            Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])
            ```` 
        * argparse.REMAINDER #搜集剩余的参数
            ````python
            >>> parser = argparse.ArgumentParser(prog='PROG')
            >>> parser.add_argument('--foo')
            >>> parser.add_argument('command')
            >>> parser.add_argument('args', nargs=argparse.REMAINDER)
            >>> print(parser.parse_args('--foo B cmd --arg1 XX ZZ'.split()))
            Namespace(args=['--arg1', 'XX', 'ZZ'], command='cmd', foo='B')
            ````

    * const #常量
    * default #默认值
    * type #接受参数转换为的类型
    * choices #参数容许值的容器
    * required #是否省略命令行选项
    * help #帮助文档中对这个参数的描述
    * metavar #使用消息中参数的名称
    * dest #定义parse_args() 解析参数后返回对象的属性名称  

1. 简单示例添加一个参数
````python
import argparse
#定义参数解析器
parse = argparse.ArgumentParser(prog='ls',add_help=True,description="ls 查看文件目录")
#为解析器添加可识别参数
parse.add_argument("path") #添加一个位置参数
#args = parse.parse_args() #分析参数
args = parse.parse_args(["/abcd"]) 
#打印解析的参数
print(args.path)
````  
执行结果为：   
![argparse002](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/argparse002.jpg)    
2. 如果需要path可有接受多个参数。如下定义：
````python
import argparse
#定义参数解析器
parse = argparse.ArgumentParser(prog='ls',add_help=True,description="ls 查看文件目录")
#为解析器添加可识别参数
parse.add_argument("path",nargs="+") #至少接受一个位置参数
#args = parse.parse_args() #分析参数
args = parse.parse_args("./ ./abc".split()) 
#打印解析的参数
print(args.path)
````    
执行结果如下:   
![argparse003](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/argparse003.jpg)   
3. 如果需要path设置为带默认值的参数，可有如下设计：
````python
parse.add_argument("path",default="./") 
```` 
4. 添加选项参数
````python
import argparse
import argparse
parse = argparse.ArgumentParser(prog="ls",add_help=False) #不添加-h参数
parse.add_argument("-h","--help",action="store_true") #添加-h参数,当出现-h时，-h值为True，否则为FAalse
parse.add_argument("-g","--Good",action="store_false",dest="good") #当设置dest属性值时，获取的值会映射到属性dest所指向的名称上。
args = parse.parse_args("")
print(args.help,args.good)
````  
运行结果如下：  
![argparse004](https://raw.githubusercontent.com/1263351411/xdd.github.io/master/img/python/argparse004.jpg)