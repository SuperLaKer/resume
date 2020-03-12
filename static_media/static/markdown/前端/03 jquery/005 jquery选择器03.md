```html
    <script type="text/javascript" src="js/jquery-1.12.4.min.js"></script>
    <script type="text/javascript">
        $(function () {

            var $div = $("div");  //$("div").has("p").css({});
            $div.css({"backgroundColor":"gold"});

            $div.has("p").css({"fontSize":"30px"});

            $div.eq(3).css({"textIndent":"20px"});  //过滤

            $div.eq(3).prev().css({"color":"red"});  //div前面那个

            $div.find(".tip").css({"fontSize":"30px"});  //div中有类属性（tip）的  
        });
    </script>
</head>
<body>
    <div>1</div>
    <div><p>2(含有p标签)</p></div>
    <div>3:prev()</div>
    <div>4:eq(3)</div>
    <div>5</div>
    <div>6</div>
    <div>7<span class="tip">77($div.find(".tip"))</span></div>
    <div>8</div>

</body>
```

