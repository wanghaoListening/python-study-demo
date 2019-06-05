# -*- coding: utf-8 -*-
import re

from bs4 import BeautifulSoup
from urllib.parse import urljoin
"""
html的解析器对指定的页面数据进行解析
注意urllib.parse在2.x版本的引用方式不同
@staticmethod我们就知道这个方法并不需要依赖对象本身的状态。
python字符串的连接方式
http://www.openstack.org.cn/bbs/forum.php?mod=viewthread&tid=506
"""


class HtmlParser(object):

    def __get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        node_title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = node_title.get_text()
        node_summary = soup.find('div', class_='lemma-summary')
        res_data['summary'] = node_summary.get_text()
        return res_data

    def __get_new_urls(self, page_url, soup):
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        new_urls = set()
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            print("the new full_url is %s" % new_full_url)
            new_urls.add(new_full_url)
        return new_urls

    def parse(self, html_data, page_url):
        if html_data is None:
            return
        soup = BeautifulSoup(html_data, 'html.parser', from_encoding='utf-8')
        new_urls = self.__get_new_urls(page_url, soup)
        new_data = self.__get_new_data(page_url, soup)
        return new_urls, new_data

