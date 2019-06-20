"""
从“搜狐体育”上获取NBA新闻标题和链接的爬虫


通过上面的例子，我们对爬虫已经有了一个感性的认识，在编写爬虫时有以下一些注意事项：

处理相对链接。有的时候我们从页面中获取的链接不是一个完整的绝对链接而是一个相对链接，这种情况下需要将其与URL前缀进行拼接（urllib.parse中的urljoin()函数可以完成此项操作）。

设置代理服务。有些网站会限制访问的区域（例如美国的Netflix屏蔽了很多国家的访问），有些爬虫需要隐藏自己的身份，在这种情况下可以设置使用代理服务器，代理服务器有免费（如西刺代理、快代理）和付费两种（如讯代理、阿布云代理)，
付费的一般稳定性和可用性都更好，可以通过urllib.request中的ProxyHandler来为请求设置代理。

限制下载速度。如果我们的爬虫获取网页的速度过快，可能就会面临被封禁或者产生“损害动产”的风险（这个可能会导致吃官司且败诉），可以在两次下载之间添加延时从而对爬虫进行限速。

避免爬虫陷阱。有些网站会动态生成页面内容，这会导致产生无限多的页面（例如在线万年历通常会有无穷无尽的链接）。可以通过记录到达当前页面经过了多少个链接（链接深度）来解决该问题，当达到事先设定的最大深度时爬虫就不再像队列中添加该网页中的链接了。

SSL相关问题。在使用urlopen打开一个HTTPS链接时会验证一次SSL证书，如果不做出处理会产生错误提示“SSL: CERTIFICATE_VERIFY_FAILED”，可以通过以下两种方式加以解决：

使用未经验证的上下文

import ssl

request = urllib.request.Request(url='...', headers={...})
context = ssl._create_unverified_context()
web_page = urllib.request.urlopen(request, context=context)
设置全局的取消证书验证

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
"""

from urllib.error import  URLError
from urllib.request import urlopen


import re
import pymysql

from pymysql import Error

import ssl



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
def get_page_html(seed_url,*,retry_times=3,charsets=('utf-8',)):
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(),charsets)
    except URLError:
        if retry_times > 0:
            get_page_html(seed_url, retry_times=retry_times - 1,
                                 charsets=charsets)
    return page_html


# 从页面中提取需要的部分(通常是链接也可以通过正则表达式进行指定)

def get_matched_parts(page_html,pattern_str,pattern_ignore_case=re.I):
    pattern_regex = re.compile(pattern_str, pattern_ignore_case)
    return pattern_regex.findall(page_html) if page_html else []



# 开始执行爬虫程序并对指定的数据进行持久化操作

def start_crawl(seed_url, match_pattern, *, max_depth=-1):
    conn = pymysql.connect(host='localhost', port=3306,
                           database='python_demo', charset='utf8',
                           user='root', password='wh6532140')

    try:
        with conn.cursor() as cursor:
            url_list = [seed_url]
            # 通过下面的字典避免重复抓取并控制抓取深度
            visited_url_list = {seed_url:0}
            while url_list:
                current_url = url_list.pop(0)
                depth = visited_url_list[current_url]
                if depth <= max_depth:
                    # 尝试用utf-8/gbk/gb2312三种字符集进行页面解码
                    page_html = get_page_html(current_url,charsets=('utf-8', 'gbk', 'gb2312'))
                    links_list = get_matched_parts(page_html,match_pattern)
                    param_list = []
                    for link in links_list:
                        if link not in links_list:
                            visited_url_list[link] = depth+1
                            page_html = get_page_html(link,charsets=('utf-8', 'gbk', 'gb2312'))
                            headings = get_matched_parts(page_html,r'<h1>(.*)<span')
                            if headings:
                                param_list.append((headings[0], link))
                    cursor.executemany('insert into tb_result values (default, %s, %s)',param_list)
                    conn.commit()

    except Error:
        pass
    finally:
        conn.close()


def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl('http://sports.sohu.com/nba_a.shtml',
                r'<a[^>]+test=a\s[^>]*href=["\'](.*?)["\']',
                max_depth=2)

if __name__ == '__main__':
    main()
