#### display属性

display属性是用来设置元素的类型及隐藏的，常用的属性有：
1、none 元素隐藏且不占位置
2、block 元素以块元素显示
3、inline 元素以内联元素显示
4、inline-block 元素以内联块元素显示

```html
    <title>display</title>
    <style type="text/css">
        body{
            margin: 0;
        }
        .div1{
            font-size: 0px;
        }
        .div1 div{
            display: inline-block;
            width: 200px;
            height: 100px;
            border: black 1px solid;
            background-color: gold;
            font-size: 16px;
            margin-right: -1px;
            line-height: 100px;
            text-align: center;
        }
        .div2{
            width: 120px;

        }
        .div2 h3{
            font-size: 30px;
        }
        .div2 div{
            width: 200px;
            height: 200px;
            background-color: gold;
            font-size: 16px;
            display: none;
        }
        .div2:hover div{
            display: block;
        }
    </style>
</head>
<body>
    <div class="div1">
        <div>1</div>
        <div>2</div>
        <div>3</div>

        <br />
        <br />
    </div>
<div class="div2">
    <h3>文字标题</h3>
    <div>文字标题说明</div>
</div>
```

