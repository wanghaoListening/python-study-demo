
#装饰器

def now():
    print('2015-3-25')

f = now

#函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)
print(f.__name__)

'''
假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修
改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
'''

def log(func):
    def wrapper(*args,**kw):
        print('call function %s()'%func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now_time():
    print('2018-10-11')

#把@log放到now()函数的定义处，相当于执行了语句now = log(now)

'''
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先
打印日志，再紧接着调用原始函数。
'''

def logV2(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('hello world')
def now_time_v2():
    print('2015-3-25')

#和两层嵌套的decorator相比，3层嵌套的效果是这样的：now = log('hello world')(now)

#注意：经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
print(now.__name__)

#Python内置的functools.wraps可以解决函数名修饰后变化的问题

import functools

def logv(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call function %s()'%func.__name__)
        return func(*args,**kw)
    return wrapper

def logV3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

#只需在定义wrapper()的前面加上@functools.wraps(func)即可


#问题设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

import time
def metric(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('start time %s' %(time.time()))
        start = time.time()
        func(*args,**kw)
        end = time.time()
        print('exec time %s'%(end-start))
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

'''

'''