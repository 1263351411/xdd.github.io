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





















