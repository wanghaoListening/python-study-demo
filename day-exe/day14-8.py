"""
Python中实现并发编程的三种方案：多线程、多进程和异步I/O。并发编程的好处在于可以提升程序的执行效率以及改
善用户体验；坏处在于并发的程序不容易开发和调试，同时对其他程序来说它并不友好。

多线程：Python中提供了Thread类并辅以Lock、Condition、Event、Semaphore和Barrier。Python中有GIL来
防止多个线程同时执行本地字节码，这个锁对于CPython是必须的，因为CPython的内存管理并不是线程安全的，因为
GIL的存在多线程并不能发挥CPU的多核特性。
"""

"""
面试题：进程和线程的区别和联系？
进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
线程 - 操作系统分配CPU的基本单位
并发编程（concurrent programming）
1. 提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
2. 改善用户体验 - 让耗时间的操作不会造成程序的假死
"""


import glob
import os
import threading

from PIL import Image

PREFIX = 'thumbnails'


def generate_thumnail(infile,size,format='PNG'):
    """生成指定图片文件的缩略图"""
    file,ext = os.path.splitext(infile)
    #find() 返回字符串最后一次出现的位置
    file = file[file.rfind('/')+1:]
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfile,format)



def main():
    """主函数"""
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    # glob 文件名模式匹配，不用遍历整个目录判断每个文件是不是符合。
    for infile in glob.glob('images/*.png'):
        for size in (32, 64, 128):
            # 创建并启动线程
            threading.Thread(
                target=generate_thumnail,
                args=(infile, (size, size))
            ).start()


if __name__ == '__main__':
    main()
