# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/4/30 16:55'

# windows10控制台默认编码gbk

import subprocess

ret = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
