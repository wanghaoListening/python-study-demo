"""
在Python语言中，单线程+异步I/O的编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。
协程最大的优势就是极高的执行效率，因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销。
协程的第二个优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不
用加锁，只需要判断状态就好了，所以执行效率比多线程高很多。如果想要充分利用CPU的多核特性，最简单的方法是多
进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
"""

"""
创建了一个列表容器然后填入了100000000个数，这一步其实是比较耗时间的，所以为了公平起见，当我们将这个任务分
解到8个进程中去执行的时候，我们暂时也不考虑列表切片操作花费的时间，只是把做运算和合并运算结果的时间统计出来
"""

from multiprocessing import Process,Queue
from random import randint
from time import time


def task_handle(cur_list,task_queue):
    total = 0
    for ele in cur_list:
        total+=ele
    task_queue.put(total)



def main():
    processes = []
    number_list = [x for x in range(1,100000001)]
    task_queue = Queue()
    index = 0
    for _ in range(8):
        p = Process(target=task_handle,args=(number_list[index:index + 12500000], task_queue))
        index+=12500000
        processes.append(p)
        p.start()

    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not task_queue.empty():
        total+=task_queue.get()

    print(total)
    end = time()
    print((end-start))


if __name__ == '__main__':
    main()



