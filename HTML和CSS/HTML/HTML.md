# HTML

* HTML（超文本标记语言——HyperText Markup Language），它使用标签来定义文本的显示方式。简单来说， HTML就是一种文本文件，里面的内容超出一般文本文件表示，它是用来控制显示格式和对内容进行排版的。  

* 1997年W3C发布HTML 4.0。  
* 2014年发布HTML5 。  

## 标签Tag

````html
<p>这是分段</p>
<h1>这是大标题</h1>
<a href="www.magedu.com" target="_blank">这是链接</a>
````  

* 如上， `<p>` 中的p就是标签，且是开始标签， `</p>` 是结束标签。开始、结束标签和内容组成完整的元素。 `<p>` 标签，它的作用范围是下一个和它层次对应的结束标签 `</p>` 。
* href和target是标签的属性。
* `<p />` 空元素可以在开始标签中关闭，也可以 `<p></p>` 。由于p标签是容器标签，在 `<p></p>` 中间可以插入其它 标签。  
* 在HTML中使用单独标签，例如 `<br><hr> <img>` 等。它们中就不能插入其它标签
* 标签名可以使用大小写，但是推荐使用小写。
* 标签会被解析成一个有层次的DOM树，不要出现标签交错的现象，这是错误的，但是浏览器有容错能力，但是可能显示的格式就不对了。  

## HTML文档结构

* 文档声明：`<!DOCTYPE html>`声明文档类型，这是Html5的声明方式。早期的文档声明很长，规定了HTML遵从的规范，能自动检查错误等。  
* 根标签：html标签是根标签
* 头部：head标签就是头部，一般不是用来显示
    1. 内部可以写meta信息、title网页标题、script脚本、样式表等标签
    2. `<meta charset="utf-8">`定义网页编码格式为utf-8。浏览器会按照这个编码显示字符。
* 正文：body标签才是浏览器显示的正文部分

## 常用标签

1. **链接**

    ````html
    <a href="http://www.xdd.com" target="_blank" onclick="alert('anchor')">这是链接</a>
    ````

    * href属性：指定链接。
    * target属性，指定是否在本窗口中打开。`_blank`表示在新窗口打开链接。
    * **onclick**是点击事件，等号后面往往写一个js函数或脚本执行。很多HTML标签都支持很多**事件属性**,常见有onclick、ondblclick、onkeydown、onkeyup、onkeypress、onmousedown、onmousemove、onmouseover、onsubmit、onchange等等。后面写的函数称作事件响应函数或事件回调函数。
    * 默认情况下超链接点击后会发起一个HTTP GET请求。
2. **图片**

    ````html
    <img src="http://www.xdd.com/abc.jpg">
    ````

    * 图片标签，src指定图片路径。注意，图片会发起一个HTTP GET请求。

3. **标题** `<h1>~<h6>`,标题标签，默认h1字体最大，h6字体最小。
4. **图层**

    ````html
    <div id="logo" class="logo"></div>
    ````

    * id属性，非常重要，标签的唯一标识
    * class属性，非常重要，样式标定位附加样式。
    * `<div>`标签，目前该标签加上css,被广泛用于网页布局中。
5. **列表**
    * 无序列表

    ````html
    <ul>
        <li>Coffee</li>
        <li>Milk</li>
    </ul>
    ````

    * 有序列表

    ````html
    <ol>
        <li>Coffee</li>
        <li>Milk</li>
    </ol>
    ````

6. **表格**
    * HTML表格的基本结构：
        1. `<table>...</table>`定义表格
        2. `<tr>...</tr>`定义表格的行
        3. `<th>...</th>`定义表格的标题列(文字加粗)
        4. `<td>...</td>`定义表格的列

    ````html
    <table border="1">
        <tr>
            <th>1,1</th>
            <th>1,2</th>
        </tr>
        <tr>
            <td>2,1</td>
            <td>2,2</td>
        </tr>
        <tr>
            <td colspan="2">占2列</td>
        </tr>
    </table>
    ````

7. **表单**

    ````html

    ````







