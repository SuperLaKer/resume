```
两个div之间的上边距
margin-buttom：20px  和 margin-top:30px 真正的距离为两者较大的(30px不是50px)
```

1. 使用这种特性
2. 设置一边的外边距，一般设置margin-top
3. 将元素浮动或者定位

```html
    <title></title>
    <style type="text/css">
        .box{
            width: 500px;
            border: black 1px solid;
            margin: 50px auto;
        }
        .box div{
            /*margin-left: 20px;
            margin-right: 20px;
            margin-bottom: 20px;
            margin-top: 20px;*/
            margin: 20px;
            line-height: 20px;
        }
    </style>
</head>
<body>
<div class="box">
    <div>虽然GTX 1660 Ti本身GDP极低，并不需要太强大的散热设备。
        但是市面上的非公产品几乎全都清一色拥有庞大的体型，除了今天我们要评测的这一款映众GTX 1660 Ti黑金至尊。
    </div>
    <div>
        虽然GTX 1660 Ti本身GDP极低，并不需要太强大的散热设备。
        但是市面上的非公产品几乎全都清一色拥有庞大的体型，除了今天我们要评测的这一款映众GTX 1660 Ti黑金至尊。
    </div>
    <div>虽然GTX 1660 Ti本身GDP极低，并不需要太强大的散热设备。
        但是市面上的非公产品几乎全都清一色拥有庞大的体型，除了今天我们要评测的这一款映众GTX 1660 Ti黑金至尊。
    </div>
    <div>
        虽然GTX 1660 Ti本身GDP极低，并不需要太强大的散热设备。
        但是市面上的非公产品几乎全都清一色拥有庞大的体型，除了今天我们要评测的这一款映众GTX 1660 Ti黑金至尊。
    </div>
</div>
</body>
```

