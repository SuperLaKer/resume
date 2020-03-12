```
class Books(View):
	def get(self, request):  # get所有书籍
		pass
	def post(self, request):  # 添加书籍
		pass

class BooksDetail(View):
	def get(self, request, id):  # 查看为id的某一本数据
		pass
	def put(self, request, id):  # 编辑或更新某一本书籍
		pass
	def delete(self, request, id)  # 删除某一本书籍
		pass
```

