借助富文本编辑器，网站的编辑人员能够像使用offfice一样编写出漂亮的、所见即所得的页面。此处以tinymce为例，其它富文本编辑器的使用也是类似的。

```python
pip instrall django-tinymce
```

- 1、添加应用

  - `settings.py  INSTALLED_APPS=('tinymce',)`

- 2、添加编辑器配置

  ```python
  TINYMCE_DEFAULT_CONFIG = {
      'theme': 'advanced',
      'width': '600',
      'height': '400',
  }
  ```

- 3、在url.py中配置编辑器url

  ```python
  urlpatterns = [
      ...
      url(r'^tinymce/', include('tinymce.urls')),
  ]
  ```

  

