"""
要实现跨平台的多进程编程，可以使用multiprocessing模块的Process类来创建子进程，而且该模块还提供了更高级的
封装，例如批量启动进程的进程池（Pool）、用于进程间通信的队列（Queue）和管道（Pipe）
"""

from multiprocessing import Process
from os import getpid
from random import randint
from time import time,sleep

def down_task(filename):
    print('启动下载进程，进城号[%d]' %getpid())
    print('开始下载%s...' %filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成，耗费%d秒' %(filename,time_to_download))



def main():
    start = time()
    p1 = Process(target=down_task,args=('python web 开发指南',))
    p1.start()
    p2 = Process(target=down_task, args=('java 开发指南',))
    p2.start()
    #等待进程执行结束
    p1.join()
    p2.join()
    end = time()
    print('总共花费 %.2f秒' %(end-start))

if __name__ == '__main__':
    main()
