理解：耗时任务影响代码执行（能否使用go？代码执行结束，go协程也没了

恶意攻击容易蹦）

任务发出者===》任务队列broker《==监听任务==任务执行者worker

```
pip install celery
```

#### 找一个服务器专门发邮件

```python
# 使用celery
from celery import Celery
from django.core.mail import send_mail

app = Celery('celery_tasks.tasks', broker="redis://127.0.0.1:6379/3")

# 定义任务函数
@app.task
def celery_send_mail(to_email, username, html_message):
    """发送激活邮件"""
    subject = "测试信息"
    message = ""
    from_mail = username
    receiver = [to_email]
    html_message = html_message
    send_mail(subject, message, from_mail, receiver, html_message=html_message)
```

```python
def sendmail(request):
    subject = "测试信息"
    message = "点击激活"
    from_mail = "944162982@qq.com"
    receiver = ['944162982@qq.com']
    html_message = "http://www.baidu.com"  # 关键字参数

    celery_send_mail.delay(receiver, from_mail, html_message)
    return HttpResponse("hello")

```

#### 配置worker

- 拷贝代码到的其他电脑
- `cd 文件夹`
- `celery -A celery_tasks.tasks worker -l info`# 显示提示信息
- 