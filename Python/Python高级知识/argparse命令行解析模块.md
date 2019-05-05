# argparse命令行解析模块
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
    * **argument_default**
    * **confict_handler**
    * **add_help**  #是否自动为解析器增加-h和--help选项，默认值为True
    * **allow_abbrev**
    