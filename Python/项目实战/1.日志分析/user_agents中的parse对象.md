@[toc]
# user_agents模块中的parse对象
## 安装  
> pip install pyyaml user-agents ua-parser
* useragent分析器。  
useragent指的是，软件安装一定的格式向远端的服务器提供一个标识自己的字符串。在HTTP协议中，使用user-agent字段传送这个字符串。  
注意：这个值可以被修改  
## 格式：  
* 现在浏览器的user-agent值格式一般如下：
````
 Mozilla/[version] ([system and browser information]) [platform] ([platform details]) [extensions]
````
* 例如： 
````
Chrome Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
 
Firefox Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0 Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
 
IE Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)
````

## 使用
````python
from user_agents import parse
 
useragents = [    
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)" ]

for uastring in useragents:    
    ua = parse(uastring)    
    print(ua.browser, ua.browser.family, ua.browser.version, ua.browser.version_string)
````

* 运行结果 
````
Browser(family='Chrome', version=(57, 0, 2987), version_string='57.0.2987') Chrome (57, 0, 2987) 57.0.2987   
Browser(family='Firefox', version=(56, 0), version_string='56.0') Firefox (56, 0) 56.0   
Browser(family='Firefox', version=(52, 0), version_string='52.0') Firefox (52, 0) 52.0 
Browser(family='IE', version=(10, 0), version_string='10.0') IE (10, 0) 10.0
````   
ua.browser.family和ua.browser.version_string分别返回浏览器名称、版本号。