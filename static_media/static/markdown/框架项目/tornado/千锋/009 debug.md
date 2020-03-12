#### debug=True

- 自动重启
  - 监控源代码文件，当有保存改动时会自动重启
  - 保存后有代码错误，会自动重启失败
  - 可以通过`autoload=True`去设置，仅仅自动重启
- 取消缓存编译的模板
  - `compiled_template_cache=False单独设置`
- 取消缓存静态文件的hash值
  - `static_hash_cache=False`
- 提供最终信息（）
  - `server_traceback=True`