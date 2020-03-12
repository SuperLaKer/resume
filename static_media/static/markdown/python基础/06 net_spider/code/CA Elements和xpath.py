# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/4/29 23:04'

from lxml import etree

text = """
<div class="collapse navbar-collapse" id="main-menu">
    <ul class="menu">
        <li class="nav-current"><a ></a></li>
        <li><a href="http://duanziwang.com/goodluck"><i class="fa fa-plane"></i>&ensp;手气不错</a></li>-->
        <li><a href="//duanziwang.com/category/%E6%90%9E%E7%AC%91%E5%9B%BE/" title="搞笑图">搞笑图</a></li>
        <li><a href="https://t.duanziwang.com/" title="丹熏山">丹熏山</a></li>
    </ul>   
</div>
"""


def main0():
    html = etree.HTML(text)  # <Element html at 0x1eeb6295fc8> 对象

    # 参看Element对象中包含的字符串
    # print(etree.tostring(html).decode())
    # 自动补全完整格式<html><body> and so on !</body></html>

    # 获取标签href 和 文本
    result = html.xpath("//li[@class='nav-current']/a/@href")
    result1 = html.xpath("//li[@class='nav-current']/a/text()")

    print("href:{}\ntext:{}".format(result, result1))


# 把href和文本组成字典
def main1():
    html = etree.HTML(text)

    # 方法一：直接定位到内容标签
    hrefs = html.xpath("//ul[@class='menu']/li/a/@href")  # 直接取文本内容
    texts = html.xpath("//ul[@class='menu']/li/a/text()")

    my_dict = {}
    for href in hrefs:  # href为list，里面存放的就是字符串
        my_dict["herf"] = href
        my_dict["text"] = texts[hrefs.index(href)]
        print(my_dict)


def main():
    html = etree.HTML(text)
    # 定位到内容上级中标签
    father_ul = html.xpath("//ul[@class='menu']/li/a")
    print(father_ul)  # [<Element a at 0x17313151108>, <Element a at 0x17313151208>,
    # <Element a at 0x17313151248>, <Element a at 0x17313151288>]

    my_dicts = {}
    for context_mark in father_ul:
        my_dicts["href"] = context_mark.xpath("./@href")[0] if len(context_mark.xpath("./@href")) else None
        my_dicts["text"] = context_mark.xpath("./text()")[0] if len(context_mark.xpath("./text()")) else None
        print(my_dicts)


if __name__ == '__main__':
    # main1()  # 如果herf没有了，下面的数据就会全部出错，还会异常
    main()  # 如果不存在设置为None，不会异常
