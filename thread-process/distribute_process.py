
'''
Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不
必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
'''

import random,time,queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()

#接受结果的队列
result_queue = queue.Queue()

#从basemanager 继承的queuemanager
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)

# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('',5000),authkey=b'abc')
#启动queue
manager.start()
#获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()

#放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')

'''
当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，添加任务到Queue不可
以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得
的Queue接口添加。
'''

import time,sys,queue
from multiprocessing.managers import BaseManager

#创建类似的QueueManager
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('connect to server %s...'%server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr,5000),authkey=b'abc')
#从网络连接
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')


