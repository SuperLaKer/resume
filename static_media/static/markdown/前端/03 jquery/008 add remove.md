```html
    <script type="text/javascript" src="js/jquery-1.12.4.min.js"></script>
    <script type="text/javascript">
        $(function () {

            var $div = $(".box");

            $div.addClass("back");

            $div.removeClass("big");

        });
    </script>
    <style type="text/css">

        .box{
            color: #5b61ff;
        }
        .back{
            background: #ff4534;
        }
        .big{
            font-size: 50px;
        }
    </style>
</head>
<body>
    <div class="box big">div元素</div>
```

