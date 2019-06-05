# -*- coding: utf-8 -*-
"""
html的下载器，对指定的url的页面进行下载
"""
from urllib import request


class HtmlDownloader(object):

    def download(self, new_url):
        if new_url is None:
            return None
        f = request.urlopen(new_url)
        print('Status:', f.status, f.reason)
        if f.status != 200:
            return None
        return f.read().decode('utf-8')
