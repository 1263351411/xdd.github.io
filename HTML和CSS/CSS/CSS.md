# CSS （Cascading Style Sheet）

层叠样式表，控制HTML的布局和样式。

## 使用方法

1. 三种使用方式
    * 内联样式：在标签内使用属性stype
    * 页内样式：在`<head>`标签中使用`<stype type='text/css'></style>`
    * 外部样式：使用CSS文件，使用`<link rel="stylesheet" type="text/css" href="mystyle.css"`

* 优先级从高到低。

## 基本语法

* `selector {property1:value1,...,propertyN:valueN}`

1. 例如：`a {color:red;text-decoration:line-through}`,将连接标签文字颜色变成红色且有横线穿过。

* **颜色写法**

````css
p { color:#ff0000;} /**大小写无所谓**/
p { color:#f00;} /**FF0000的缩写**/
p { color: rgb(255,0,0);} /****/
````

## 选择器

1. **标签选择器**
    * 例如：`body {text-align:center}`
    1. 上例直接使用HTML标签的选择器，就是标签选择器，元素选择器。
    2. **注意：如果将标签改为*，表示匹配所有HTML标签。**
2. **id选择器**
    * id指的是HTML标签内的属性id,例如`<div id="menu">`。

    ````css
    #menu {
        background-color:rgb(255,255,255);
        width:100%;
        border-bottom:#f0f0f0 solid 1px;
        margin:0px 0px 5px 0px;
    }
    ````

3. **类选择器**
    * 类，指的是标签中的class属性，例如：`<div class='main center'>`

    ````css
    .center {
        width:80%;
        margin:auto;
    }
    ````

4. **选择器分组**
    * 分组的选择就可以使用同样的样式声明

    ````css
    h1,h2,h3,h4,h5,h6 {
        color:green;
    }
    ````

5. **层次选择器**
    1. **后代选择器**
        * 所有div任意层次下的li标签

        ````css
        div li { /**所有div任意层次下的li标签**/
            display:inline;
        }
        ````

        * div中id是menu下的li标签

        ````css
        div#menu li {
            display:inline;
        }
        ````

    2. **子选择器**
        * ul标签下的直接子标签li(中间不能间隔其他标签)

        ````css
        ul > li {
            display:inline;
        }
        ````

        * div中id为menu 下的ul标签，并且ul下的直接子标签li

        ````css
        div#menu ul > li {
            display:inline;
        }
        ````

    3. **相邻兄弟选择器**
        * class为detail的div标签下任意层下的近邻标签的下一个p标签

        ````css
        div.detail p + p{
            color:green;
        }
        ````

## 伪类 pseudo-classes

* 伪类能增加样式，类似于class
* 锚伪类，链接标签a的四种状态

````css
a:link {color:red} /* 未访问的链接 */
a:visited {color: green} /* 已访问的链接 */
a:hover {color: blue} /* 鼠标移动到链接上 */
a:active {color: black} /* 选定的链接 */
````

* 伪类可以和css类配合使用

````css
a.red:visited {color:#ff0000} /**a标签中带有属性red的标签，修改已访问的链接颜色**/
a:hover { color:red;} /** 定义所有a标签，鼠标移动到链接上后a标签中的颜色 **/
a {
    color:chartreuse;
    text-decoration-line:none;
}

<a class = "red" href="css_syntax.asp">CSS Syntax</a>
````  

注意，伪类和前面部分中间不要有空格。

## 伪元素pseudo-element

* 伪元素能增加元素
    1. `:before`，`:after`可以在元素前后插入内容

    ````css
    #homepage:after {
        content:url(http://www.xdd.com/abc.png);
    }
    a:before {
        content:"这是链接~~~~~~";
    }
    ````

## 属性选择器

|语法|含义|
|:-----|:-----------|
E[attr]{sRules}|具有某属性
E[attr=value]{sRules}|具有某属性且等于value
E[attr ~= value]{sRules}|具有某属性且属性值中的一个是value
E[attr \|= value]{sRules}|具有某属性且属性值使用了`-`，且`-`之前的部分是value的才匹配<br/>`*[class|="main"]`能和`<div class='main-center'>`减号之前的部分匹配

````css
/*链接具有href属性*/
a[href]{
    color:blue;
    text-decoration:line-through
}

/*图片alt属性为xdd*/
img[alt=xdd]{
    height:20px;
}

/*所有标签中class完全等价于“main center”的标签*/
*[class="main center"]{
    color:black
}

/* 对所有标签中，具有center属性的标签*/
*[class~="center"]{
    color:black
}
````

## 继承

````css
body{
    text-align:center;
    color:red;
}
````

* 观察整个页面文字颜色，几乎变成了红色。
* 页面中父元素中使用的样式。通过css继承，子孙元素将继续并使用祖先元素的属性，除非子元素重新定义了该属性。

## 常见样式

* 背景backgroud复合属性[http://www.w3school.com.cn/css/css_background.asp](http://www.w3school.com.cn/css/css_background.asp)
* 字体font复合属性[http://www.w3school.com.cn/css/css_font.asp](http://www.w3school.com.cn/css/css_font.asp)

* 表格border

````css
table {
    border-collapse:collapse;
}

table,td {
    border:1px solid black;
}
````

* margin外边距和padding内边距

````css
margin: top right bottom left
padding: top right bottom left

padding:10px 2px 15px 20px; /**顺时针上右下左**/
padding:10px 5px 15px; /*上10px、左右5px、下15px*/
padding:10px 5px; /*上下10px、左右5px*/
padding:10px /*4个方向全是10px*/
margin:auto /*浏览器自动计算边距*/
````

* 内外边距都是顺时针设置4个方向，也可以单独设置。

## 测试用HTML

````html
<html>

<head>
    <title>test page</title>
    <meta charset="utf-8">
    <style type="text/css"> </style>
</head>

<body>
    <div class='main center'>
        <div id="menu">
            <ul>
                <li><a id="homepage">主页</a></li>
                <li><a>Linux</a></li>
                <li><a>Python</a></li>
            </ul>
        </div> <a href="http://www.magedu.com" target="_blank" title="abc">请点击</a><span>inline span</span>
        <p> <span>biggest title</span>
            <img src="http://www.magedu.com/wp-content/uploads/2017/09/logo.png" alt="magedu_logo"> </p>
        <div id='detail' name='detail' class="detail">
            <p>title</p>
            <p>content</p>
        </div>
        <div>
            <form action="" method="POST">
                <table>
                    <tr>
                        <td>用户名<input name='h' type="hidden" value="001111256"></td>
                        <td><input name='username' type="text" value="abc"></td>
                    </tr>
                    <tr>
                        <td>密码</td>
                        <td><input name='pwd' type="password"></td>
                    </tr>
                    <tr>
                        <td>性别</td>
                        <td><input name=gender type="radio" checked value="M">男<input name=gender type="radio"
                                value="F">女</td>
                    </tr>
                    <tr>
                        <td>爱好</td>
                        <td> <input name="interest" type="checkbox" checked value="music">音乐 <input name="interest"
                                type="checkbox" checked value="movie">电影 </td>
                    </tr>
                    <tr>
                        <td>其他</td>
                        <td> <textarea> line1 line2 </textarea> </td>
                    </tr>
                    <tr>
                        <td colspan="2"> <input name=submit type="submit" value="提交"> <input type="reset" value="重置">
                        </td>
                    </tr>
                </table>
            </form>
        </div>
    </div>
</body>
</html>
````




















