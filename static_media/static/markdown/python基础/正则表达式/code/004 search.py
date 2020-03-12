import re

ret = re.search(r"\d+", "你好北京666").group()

print(ret)