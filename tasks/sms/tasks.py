"""
tasks这个名字
"""
import os
import django
from tasks.main import celery_app
from django.conf import settings
from django.core.mail import send_mail
#
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume.settings")
django.setup()


@celery_app.task
def send_message(message):
    # print(message*10)
    subject = "招聘信息"
    message = message
    sender = settings.EMAIL_FROM
    receiver = ["The163addr@163.com", "944162982@qq.com", "2719881771@qq.com"]
    send_mail(subject, message, sender, receiver)
