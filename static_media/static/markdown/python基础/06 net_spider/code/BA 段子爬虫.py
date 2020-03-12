# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/4/29 18:13'

import requests
import re


class DuanZi(object):
    def __init__(self):
        self.start_url = "https://duanziwang.com/page/{}/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                                      "(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    def set_url(self):
        url_list = [self.start_url.format(i + 11) for i in range(10)]

        print(url_list)

        return url_list

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    # <a href="https://duanziwang.com/1799.html" class="post-title">小时候假期妈妈把游戏机放我书包里，我找了一个假期没找到…</a>
    def filter(self, html_str):
        context_list = str(re.findall("<p>(.*?)</p>", html_str))

        context_str = re.sub(",", "\r\n\r\n", str(re.sub(r"<br>|[][]", "\r\n", str(context_list))))

        return context_str

    def run(self):
        # 整合元素
        url_list = self.set_url()
        # 发送请求，获取响应
        for url in url_list:
            page_num = url_list.index(url)
            html_str = self.parse_url(url)

            # 数据过滤
            context_str = self.filter(html_str)
            # b保存数据
            file_name = "段子{}.txt".format(page_num + 1)

            with open(file_name, "a+", encoding="utf-8") as f:
                print("正在写入：%s" % file_name)
                f.write(str(context_str))


if __name__ == '__main__':
    duanzi = DuanZi()

    duanzi.run()
