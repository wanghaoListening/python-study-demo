
"""
计算机网络是独立自主的计算机互联而成的系统的总称，组建计算机网络最主要的目的是实现多台计算机之间的通信
和资源共享。今天计算机网络中的设备和计算机网络的用户已经多得不可计数，而计算机网络也可以称得上是一个“复
杂巨系统”，对于这样的系统，我们不可能用一两篇文章把它讲清楚，有兴趣的读者可以自行阅读Andrew S.Tanenbaum老师
的经典之作《计算机网络》或Kurose和Ross老师合著的《计算机网络:自顶向下方法》来了解计算机网络的相关知识。
"""

import requests
from threading import Thread
from time import time


class DownloadHanlder(Thread):

    def __init__(self,url):
        super().__init__()
        self._url = self

    def run(self):
        filename = self._url[self._url.rfind('/') + 1:]
        resp = requests.get(self._url)
        with open('/Users/admin'+filename,'wb') as f:
            f.write(resp.content)



def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要在天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码的中APIKey即可

    resp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    print(data_model)
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHanlder(url).start()


if __name__ == '__main__':
    main()


