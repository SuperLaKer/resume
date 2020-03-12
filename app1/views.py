import logging
import time
import os
import requests
import json
import threading
from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from app1.models import GetDB, PostDB
from django.http import HttpResponse
from tasks.sms.tasks import send_message

timer = str(time.time())[-5:]
addr = ["addr初始化"]


# 发送邮件
# def send_message(message):
#     subject = "招聘信息"
#     message = message
#     sender = settings.EMAIL_FROM
#     receiver = ["The163addr@163.com", "944162982@qq.com", "2719881771@qq.com"]
#     send_mail(subject, message, sender, receiver)


# 写文件
def writefile(file):
    global timer
    filepath = os.path.join(settings.MEDIA_ROOT, timer + file.name)
    f = open(filepath, "wb")
    print(filepath)
    for line in file.chunks():
        f.write(line)
    f.close()


# 获取位置信息
def get_addr(ip):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"
    }
    ip = ip
    url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?" \
          "query={}&resource_id=6006&tn=baidu&format=json&" \
          "ie=utf-8&oe=utf-8&need_di=1&_=1560477373226&cb=json".format(ip)
    try:
        r = requests.get(url, headers, timeout=0.5)
    except Exception as e:
        logging.error(e)
        logging.error("**********timeout**************")
        addr[0] = "timeout"
    else:
        try:
            temp = json.loads((r.content.decode())[9:-2]).get("data")[0].get("location")
        except Exception as e:
            logging.error(e)
            addr[0] = "raise sth"
        else:
            addr[0] = temp


# 数据库记录
def write_get_db(ip, address):
    try:
        GetDB.objects.create(ip=ip, address=address)
    except Exception as e:
        logging.error(e)


# 数据库记录
def write_post_db(ip, address, message, file_name):
    try:
        PostDB.objects.create(ip=ip, address=address, message=message, file_name=file_name)
    except Exception as e:
        logging.error(e)


# Create your views here.
class ResumeView(View):
    """注册类视图"""

    def get(self, request):
        ip = request.META.get("REMOTE_ADDR")
        # 获取位置信息
        t1 = threading.Thread(target=get_addr, args=(ip,))
        t1.start()
        time.sleep(0.5)
        t2 = threading.Thread(target=write_get_db, args=(ip, addr[0]))
        t2.start()

        return render(request, "index.html")

    def post(self, request):  # 和用户注册逻辑相同
        """进行注册逻辑"""
        ip = request.META.get('REMOTE_ADDR')
        message = str(request.POST.get("message"))
        file = request.FILES.get('file')
        # 获取位置信息
        # t6 = threading.Thread(target=get_addr, args=(ip,))
        # t6.start()
        if file is not None:  # 文件不为空，信息也不为空
            new_message = message + "*" * 5 + timer + str(file.name)

            # 发送邮件
            send_message.delay(new_message)
            # t1 = threading.Thread(target=send_message, args=(new_message,))
            # t1.start()

            # 写文件
            t2 = threading.Thread(target=writefile, args=(file,))
            t2.start()
            # 写数据库
            t3 = threading.Thread(target=write_post_db, args=(ip, addr[0], new_message, file.name))
            t3.start()
            return render(request, 'index.html')

        else:
            # 发送邮件
            send_message.delay(message)
            # t4 = threading.Thread(target=send_message, args=(message,))
            # t4.start()

            file_name = None

            t5 = threading.Thread(target=write_post_db, args=(ip, addr[0], message, file_name))
            t5.start()

            return render(request, 'index.html')


class SendMailTest(View):
    def get(self, request):
        return render(request, "sendmain.html")

    def post(self, request):
        message = request.POST.get("message", "哈哈哈")
        print(message)
        send_message.delay(message)
        return HttpResponse("ok")
