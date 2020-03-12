# coding:utf-8
"""
常用正则表达式：. *  +  ?  ()|()  (?P<name>)  (?P=name)  [a-zA-Z0-9_]  [^0-9]:除了0-9  \\d{11}
              {m,n}  \\w 字母  | 左右任意一个
"""
__author__ = "superlaker"
__date__ = '2019/4/27 12:30'

import re


# 常用
def main0():
    result = re.match(r"h.", "heheha")  # 默认匹配开头
    if result:
        print(result.group())
    else:
        print("error")


# 贪婪
def main1():
    result0 = re.match(r"<.*>", "<h1>heheda</h1>")  # 贪婪匹配<h1> or <h1>heheda</h1>
    result1 = re.match(r"<.*?>", "<h1>heheda</h1>")  # 非贪婪匹配 ?  匹配0次 or 1次

    html_str = """<div>
        <p>岗位职责：</p>&nbsp;
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br>&nbsp;</p>&nbsp;
<p>必备要求：</p>&nbsp;"""

    result = re.sub(r"<.*?>|>|&nbsp;", "", html_str)

    if result:
        print(result)
    else:
        print("error")


# 分组
def main2():
    result0 = re.match(r"\w+@(qq.*|163)\.com$", "944@qqheheda.com")  # 分组和或 |

    result = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>",
                      "<html><h1>www.baidu.com</h2></html>")

    if result:
        print(result.group())
    else:
        print("error")


# findall()的用法
def main3():
    result = re.findall("a.b", "acbadb")
    result0 = re.findall("a(.+?)b", "acdbadb")
    print(result)  # ['acb', 'adb']
    print(result0)  # ['c', 'd']


# re.compile()
def main():
    p = re.compile("a.b", re.DOTALL)  # re.S
    result = p.match("a\nb").group()
    print(result)


if __name__ == '__main__':
    main3()
