```
嵌套盒子：设置 子盒子的margin-top 会影响父级盒子的margin-top
```

```
解决方法：
		父级盒子：设置border
		父级盒子：设置overflow：hidden
		使用伪类元素
```

```html
    <title>塌陷</title>
    <style type="text/css">
        .clearfix:before{/*使用伪元素*/
            content: "";/*塞进去空字符串*/
            display: table;
        }
        .con{
            width: 300px;
            height: 300px;
            background-color: gold;
            /*padding-top: 100px;*/
        }
        .box{
            width: 200px;
            height: 100px;
            background-color: green;
            margin-top: 100px;/*仅仅垂直塌陷*/
            margin-left: 50px;
        }
    </style>
</head>
<body>
<div class="con clearfix">
    <div class="box"></div>
</div>
</body>
```

