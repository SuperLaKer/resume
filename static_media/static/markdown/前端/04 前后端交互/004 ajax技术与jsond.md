#### javascript的局限性

```
由于javascript运行在前端，为保证用户的数据安全，（不能读取客户端的数据，保护用户安全）
javascript被设计为：不能操作文件的浏览器端解释性语言
```

#### 同步和异步 

#### 局部刷新（无刷新）

```
ajax可以实现局部刷新。
ajax可以自己发送http请求，不用通过浏览器的地址栏，所以页面整体不会刷新。
ajax获取到后台数据，更新页面显示数据的部分，就做到了页面局部刷新。
```

#### 同源策略

```
ajax请求的页面或资源只能是同一个域下的资源。这是在设计ajax时基于安全的考虑。
同域：相同域名，端口相同，协议相同，缺一不可
跨域（浏览器的同源策略造成的，是浏览器对javascript的安全限制）：浏览器从一个域名的网页去请求另一个域名的资源时，域名、端口、协议至少有一个不相同，就是跨域。
跨域问题只存在于浏览器端，不存在于服务器端。
```

```
/*错误提示*/
XMLHttpRequest cannot load https://www.baidu.com/. No  
'Access-Control-Allow-Origin' header is present on the requested resource.  
Origin 'null' is therefore not allowed access.
```

#### jsonp 

```
ajax只能请求同一个域下的数据或资源，有时候需要跨域请求数据，就需要用到jsonp技术。
jsonp可以跨域请求数据，它的原理主要是利用了<script>标签可以跨域链接资源的特性。
jsonp和ajax原理完全不一样，不过jquery将它们封装成同一个函数。
```

