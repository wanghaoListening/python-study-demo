# -*- coding: utf-8 -*-
"""
对数据进行收集和处理
"""


class HtmlOutPuter(object):

    def __init__(self):
        self.datas = []

    def collect(self, p_data):
        if p_data is None:
            return
        self.datas.append(p_data)

    def output_html(self):
        for data in self.datas:
            print("title",data.get('title').encode('utf-8'))
            print("summary", data.get('summary').encode('utf-8'))
