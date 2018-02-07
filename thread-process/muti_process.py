
#多进程

'''
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操
作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程
只需要调用getppid()就可以拿到父进程的ID。
Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程

由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？

由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。

multiprocessing模块提供了一个Process类来代表一个进程对象
'''

from multiprocessing import Process

import os

#子进程要执行的代码
def run_proc(name):
    print('run child process %s(%s)'%(name,os.getpid()))

if __name__ == '__main__':
    print('parent process %s'%(os.getpid()))
    p = Process(target=run_proc,args=('test',))
    print('child process will start')
    p.start()
    p.join()#等待子进程结束后再继续往下运行
    print('child process end')

#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动

#Pool(要启动大量的子进程，可以用进程池的方式批量创建子进程)

from multiprocessing import Pool

import os,time,random

def long_time_task(name):
    print('Run task %s (%s)...'%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random*3)
    end = time.time()
    print('Task %s runs %0.2f seconds,'%(name,(end-start)))


if __name__=='__main__':
    print('parent process %s.'%os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('waiting for all subprocess done ...')
    p.close()
    p.join()
    print('All subprocesses done')

'''
对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，
因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
p = Pool(5)
就可以同时跑5个进程。
'''

#子进程

'''
很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
'''
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

#如果子进程还需要输入，则可以通过communicate()方法输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

#进程间通信

'''
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，
提供了Queue、Pipes等多种方式来交换数据。
我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
'''

from multiprocessing import Process,Queue
import os,time,random

#写数据
def write(q):
    print('process to write %s'%os.getpid())
    for value in ['A','B','C']:
        print('put %s to queue ......'%value)
        q.put(value)
        time.sleep(random.random())

#对数据进行读
def read(q):
    print('process to read %s'%os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue'%value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

'''
在Unix/Linux下，可以使用fork()调用实现多进程。
要实现跨平台的多进程，可以使用multiprocessing模块。
进程间通信是通过Queue、Pipes等实现的。
'''

