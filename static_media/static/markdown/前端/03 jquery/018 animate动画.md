```html
    <script type="text/javascript" src="js/jquery-1.12.4.min.js"></script>
    <script type="text/javascript">
        $(function () {
            var $box = $(".box");
            var $btn = $("#btn");
            var $box2 = $(".box2");
            var $btn2 = $("#btn2");
            $btn.click(function () {
                $box.animate({"width": "600px"}, 1000, function () {
                    $box.animate({"height": "400"}, 1000, function () {
                        $box.animate({opacity: 0});
                    })
                });
            });
            $btn2.click(function () {
                $box2.stop().animate({"width": "+=100"})
            })
        });
    </script>
    <style type="text/css">
        .box,.box2 {
            width: 100px;
            height: 100px;
            background-color: gold;
        }
    </style>
</head>
<body>
<input type="button" value="动画" id="btn">
<div class="box">div_box</div>
<br/>
<br/>
<input type="button" value="动画" id="btn2">
<div class="box2">div_box2</div>
</body>
```

