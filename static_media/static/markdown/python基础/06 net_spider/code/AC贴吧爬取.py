# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/4/28 0:03'
import requests


# 定义类
class TiebaSpider(object):
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.base_url = "https://tieba.baidu.com/f?kw=" + tieba_name + "+&pn={}"

        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                                     "(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    def get_url_list(self):

        url_list = [self.base_url.format(i * 50) for i in range(5)]

        # for i in range(5):
        #     base_url = self.base_url.format(self.tieba_name, i * 50)
        #     url_list.append(base_url)
        return url_list

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.header)
        return response.content.decode()

    def save_date(self, html_context, page_num):

        file_name = "{}-{}.html".format(self.tieba_name, page_num)

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(html_context)

    def run(self):
        # 构造url
        url_list = self.get_url_list()

        # 请求
        for url in url_list:
            page_num = url_list.index(url)
            html_context = self.parse_url(url)

            # 保存
            self.save_date(html_context, page_num)


if __name__ == '__main__':
    pass
    # tieba_spider = TiebaSpider("lol")
    # tieba_spider.run()
