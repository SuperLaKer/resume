## jquery属性操作

设置 标签  里面的属性  必须引号括起来

1、html() 取出或设置html内容

```
// 取出html内容
var $htm = $('#div1').html();

// 设置html内容
$('#div1').html('<span>添加文字</span>');
```

2、prop() 取出或设置某个属性的值

```
// 取出图片的地址

var $src = $('#img1').prop('src');

// 设置图片的地址和alt属性

$('#img1').prop("src": "test.jpg", alt: "Test Image" });
```

```html
    <script type="text/javascript" src="js/jquery-1.12.4.min.js"></script>
    <script type="text/javascript">

        $(function () {

            var $a = $(".link");

            alert($a.html());/*读取内容：这是一个衔接*/
            $a.html("到百度");/*更改a标签里面的内容*/
            /*读取属性*/
            console.log($a.prop("class"));

            // 设置属性
            $a.prop({"href":"https://www.baidu.com","title":"到百度"});
        });
    </script>
</head>
<body>
<a href="#" class="link">这是一个衔接</a>
</body>
```

