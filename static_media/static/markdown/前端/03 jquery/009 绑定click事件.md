```html
    <script type="text/javascript" src="js/jquery-1.12.4.min.js"></script>
    <script type="text/javascript">
    $(function () {
        var $btn = $("#btn");
        var $box = $(".box");
        $btn.click(function () {  //绑定点击事件
            if ($box.hasClass("box"))  //判断某个属性是否存在
            {
                $box.removeClass("box");
                $box.addClass("change");
            }
            else
            {
                $box.removeClass("change");
                $box.addClass("box");
            }
        })  
    });
    </script>
    <style type="text/css">

        .box{
            width: 200px;
            height: 200px;
            background-color: #5b61ff;
            font-size: 30px;
            color: gold;
        }
        .change{
             width: 200px;
            height: 200px;
            background-color: #ff4534;
            font-size: 30px;
            color: darkgreen;
        }
    </style>
</head>
<body>
    <input type="button" name="" value="切换样式" id="btn">
    <div class="box">div元素</div>
</body>
```

