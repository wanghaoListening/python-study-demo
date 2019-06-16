"""
从“搜狐体育”上获取NBA新闻标题和链接的爬虫
"""

from urllib.error import  URLError
from urllib.request import urlopen


import re
import pymysql

from pymysql import Error



# 通过指定的字符集对页面进行解码(不是每个网站都将字符集设置为utf-8)
def decode_page(page_bytes, charsets=('utf-8',)):
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass

    return page_html


# 获取页面的HTML代码(通过递归实现指定次数的重试操作)
def get_page_html(seed_html,*,retry_times=3,charsets=('utf-8',)):
    page_html = None

