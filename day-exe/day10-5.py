"""
Python中的多线程

在Python早期的版本中就引入了thread模块（现在名为_thread）来实现多线程编程，然而该模块过于底层，而
且很多功能都没有提供，因此目前的多线程开发我们推荐使用threading模块，该模块对多线程编程提供了更好的
面向对象的封装。
"""

from random import randint
from threading import Thread
from time import time,sleep

def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    thread1 = Thread(target=download,args=('python并发编程指南',))
    thread2 = Thread(target=download,args=('python web开发',))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end = time()
    print('总共花费 %.3f' %(end-start))


if __name__ == '__main__':
    main()