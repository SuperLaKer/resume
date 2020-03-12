"""这个模块名可以改为celery"""
from celery import Celery


# 定义celery对象
celery_app = Celery("resume")

celery_app.config_from_object("tasks.config")

# 自动寻找任务(tasks.py)
celery_app.autodiscover_tasks(["tasks.sms"])