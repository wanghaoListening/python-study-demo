
with open('/home/wang/examples.desktop','r') as f:
    f.read()

'''
并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
实现上下文管理是通过__enter__和__exit__这两个方法实现的
'''

class Query(object):
    def __init__(self,name):
        self.name = name
    def __enter__(self):
        print('begin')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('error')
        else:
            print('end')
    def query(self):
        print('query info about %s'%self.name)

'''
把自己写的资源对象用于with语句
'''
with Query('bob') as q:
    q.query()


#@contextmanager

'''
编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法
'''

from contextlib import contextmanager

class Query(object):

    def __init__(self,name):
        self.name = name

    def query(self):
        print('query info about %s ..'%self.name)

@contextmanager
def create_query(name):
    print('begin')
    q = Query(name)
    yield q
    print('end')

'''
@contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
'''
with create_query('bob') as q:
    q.query()

#@closing

'''
如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。
'''
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)

'''
closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
它的作用就是把任意对象变为上下文对象，并支持with语句
'''

