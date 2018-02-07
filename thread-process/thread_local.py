
#ThreadLocal

import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print('hello,%s(int %s)'%(std,threading.current_thread().name))

def process_thread(name):
    local_school = name

'''
ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样
一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
'''