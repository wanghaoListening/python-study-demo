# -*- coding: utf-8 -*-
"""
url管理器
需要维护两个url的列表：一个是已经爬取的url列表另一个是未爬取的url列表
"""


class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        elif url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def get_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def has_new_url(self):
        return len(self.new_urls) >= 0

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.new_urls.add(url)
