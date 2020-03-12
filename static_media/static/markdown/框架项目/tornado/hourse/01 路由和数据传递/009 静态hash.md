### static_url()

- 主要用在html中
- 原始
  - `<link rel="stylesheet" href="/static/style.css">`
- 使用`static_url()`
  - `<link rel="stylesheet" href="{{ static_url('css/index.css') }}">`
- 增加hash校验 `?v=hash值`
  - `<link rel="stylesheet" href="/static/style.css?v=ab12fdsafdsa">`
- 优点
  - 确保浏览器加载最新的静态文件
  - 如果使用`static_url_prefix`更改了静态路径前缀/static
  - `使用static_url()无须担心`