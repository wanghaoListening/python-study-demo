# -*- coding: utf-8 -*-
from com.haothink.baike import url_manager,html_downloader,html_parser,html_outputer


class CrawlerMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutPuter()

    def craw(self, url):
        count = 1
        self.urls.add_new_url(url)
        page_url = "http://baike.baidu.com"
        while self.urls.has_new_url:
            try:
                new_url = self.urls.get_url()
                print('craw %s is %s'%(new_url,count))
                html_data = self.downloader.download(new_url)
                p_url, p_data = self.parser.parse(html_data, page_url)
                self.urls.add_new_urls(p_url)
                self.outputer.collect(p_data)
                if count >= 1000:
                    break

                count += 1
            except Exception as e:
                print(e)

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    crawler = CrawlerMain()
    crawler.craw(root_url)
