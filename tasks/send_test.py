import os
import django
from django.core.mail import send_mail

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume.settings")
django.setup()


# from django.conf import settings


def send_message(message):
    subject = "招聘信息"
    message = message
    sender = 'python<The163addr@163.com>'
    receiver = ["The163addr@163.com", "944162982@qq.com", "2719881771@qq.com"]
    send_mail(subject, message=message, from_email=sender, recipient_list=receiver)


if __name__ == '__main__':
    send_message("haha666")