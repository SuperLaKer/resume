```html
    <script type="text/javascript" src="js/jquery-1.12.4.min.js"></script>
    <script type="text/javascript">

        $(function () {

            $div = $("#div1");
            $div2 = $(".list");

            alert($div.length);
            alert($div2.length);

            //通过length方法判断是否选到了属性，不会报错
            //选中了为1 未选中为0

        });

    </script>
</head>
<body>
    <div id="div1">div1</div>
```

