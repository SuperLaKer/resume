#### basicConfig

- 不支持中文信息处理
- 不能同时往屏幕和文件输出

```python
import logging  
logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='test.log',
                    filemode='a+')  # 追加方式
  
logging.debug('debug message')  
logging.info('info message')  
logging.warning('warning message')  
logging.error('error message')  
logging.critical('critical message')
```

代码中使用：

- 在可能出现错误的地方，加上log记录

```
try:
	int(input("num>>"))
except Exception as e:  # 捕获错误
	logging.error(e)  # 写到日志中
```

文件和屏幕都可以显示日志

```python
import logging

logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log',encoding='utf-8') 

# 再创建一个handler，用于输出到控制台 
ch = logging.StreamHandler() 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setLevel(logging.DEBUG)

fh.setFormatter(formatter) 
ch.setFormatter(formatter) 
logger.addHandler(fh) #logger对象可以添加多个fh和ch对象 
logger.addHandler(ch) 

logger.debug('logger debug message') 
logger.info('logger info message') 
logger.warning('logger warning message') 
logger.error('logger error message') 
logger.critical('logger critical message')
```

