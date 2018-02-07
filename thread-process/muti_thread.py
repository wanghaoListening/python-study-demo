

'''
由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，
并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，
对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
'''

import time,threading

def loop():
    print("the thread start....")
    n = 0
    while n<=5:
        print('thread %s => %s'%(threading.current_thread().name,n))
        time.sleep(1)
        n = n+1
    print('thread %s ended'%threading.current_thread().name)

print('thread %s is running ...'%threading.current_thread().name)
thread = threading.Thread(target=loop,name='Loopthread')
thread.start()
thread.join()
print('thread %s ended '%threading.current_thread().name)

#current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定

#Lock
'''
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于
多个线程同时改一个变量，把内容给改乱了。
'''

import time,threading

balance = 0

lock = threading.Lock()

def change_it(n):
    #先存后取
    global balance
    balance = balance +n
    balance = balance -n

def run_thread(n):
    for i in range(10000):
        lock.acquire()
        try:
           change_it(n)
        finally:
            lock.release()

'''
当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。

获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保
锁一定会被释放。
'''

#多核CPU

'''
因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，
必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程
的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。
'''

