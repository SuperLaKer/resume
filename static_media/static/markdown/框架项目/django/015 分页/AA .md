- 所有省级地区分页展示

- `from django.core.paginator import Paginator`

- `paginator = Paignator(areas, 10)`  # 每10页进行分类

  ```
  # 实例属性
  num_pages  # 分页之后的总页数
  page_range  # 返回分页后页码list
  # 实例方法
  page(self, number)  # 返回number页的Page实例对象（包含所有数据）
  ```

#### Paginator分页器

- 可以接受的参数：list，tuple，QuerySet，可以被遍历的东西

