将获取元素的语句写到页面头部，会因为元素还没有加载而出错，jquery提供了ready方法解决这个问题，它的速度比原生的 window.onload 更快。

```javascript
<script type="text/javascript" src="js/jquery-1.12.4.min.js"></script>
<script type="text/javascript">

$(document).ready(function(){
     页面加载完执行这里面的语句
});
//简写
$(function(){
     简写，页面加载完执行这里面的语句
});

</script>
```



#### ready比window.onload 快的原因

```
ready：等到标签节点加载完
window.onload：等到节点和数据加载（标签加载完成，再等渲染完成）
```

```html
<title>Document</title>
    <script type="text/javascript" src="js/jquery-1.12.4.min.js"></script>
    
	<script type="text/javascript">
        window.onload = function () {
            let oDiv = document.getElementById("div1");
            alert("原生弹出的"+oDiv);
        };

        //ready的完整写法
        $(document).ready(function () {
            let $div = $("#div1");
            alert("jquery弹出的"+$div)
        });

        //ready的简写$()相当于$(document).ready()
        $(function () {
            var $div2 = $("#div1");
            alert("ready简写"+$div2)
        });
    </script>

</head>
<body>
    <div id="div1">这是一个div元素</div>
</body>
```

