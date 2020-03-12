```
var oPos = $box.offset();
alert(oPos.left);
alert(oPos.top);

document.tittle = "自定义tittle标题";
```

```html
   <title>Title</title>
    <script type="text/javascript" src="js/jquery-1.12.4.min.js"></script>
    <script type="text/javascript">
        $(function () {
            var $box = $(".box");

            $box.click(function () {
                var oPos = $box.offset();/*每次点击重新获取位置大小*/
                document.title = oPos.left+"|"+oPos.top;
            });
        });
    </script>
    <style type="text/css">
        .box{
            width: 200px;
            height: 200px;
            background-color: #ff8200;
            margin: 50px auto 0px;
        }
    </style>
</head>
<body>
<div class="box"></div>
</body>
```

