@[toc]
# urlparse对象
导入：  
> from urllib.parse import urlparse
* urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)->ParseResult #将url解析为6个组件。
    * urlstring #需要解析的url字符串
    * scheme #寻址方案。
    * fragments #如果allow_fragments参数为false，则不能识别片段标识符。相反，它们被解析为路径、参数或查询组件的一部分，fragment被设置为返回值中的空字符串。
    * ParseResult 返回值对象，是一个元组类型的实例。
    * 简单示例
    ````python
    >>> from urllib.parse import urlparse
    >>> o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
    >>> o   # doctest: +NORMALIZE_WHITESPACE
    ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
                params='', query='', fragment='')
    >>> o.scheme
    'http'
    >>> o.port
    80
    >>> o.geturl()
    'http://www.cwi.nl:80/%7Eguido/Python.html'
    ````
## ParseResult对象
元组子类的一个实例。该类具有以下附加的只读便利属性:

Attribute|Index|Value|Value if not present
|:------|:----|:---|:-------------|
scheme| 0 |URL scheme specifier |scheme parameter 
netloc| 1 |Network location part |empty string 
path| 2 |Hierarchical path |empty string 
params| 3 |Parameters for last path element |empty string 
query| 4 |Query component |empty string 
fragment| 5 |Fragment identifier |empty string 
username|   |User name |None 
password|   |Password |None 
hostname|   |Host name (lower case) |None 
port|   |Port number as integer, if present |None 
