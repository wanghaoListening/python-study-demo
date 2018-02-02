
'''
看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类
'''

#__str__

class Student(object):

    def __init__(self,name):
        self.__name = name
    def __str__(self):
        return 'student object name %s'%(self.__name)


'''
直接敲变量不用print，打印出来的实例还是不美观，
这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

'''

#解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的,所以可以直接将__str__函数引用赋给__repr__

class Studentv2(object):
    def __init__(self,name):
        self.__name = name
    def __str__(self):
        return 'student object name %s'%(self.__name)
    __repr__ = __str__

#__iter__

'''
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就
会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
'''

#斐波那契数列

class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1 #初始化两个计数器的的值a,b
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b #计算下一个值
        if self.a > 10000:
            raise StopIteration()
        return self.a

for a in Fib():
    print(a)


#__getitem__

'''
Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行Fib()[5]
要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
'''

class FibV2(object):
    def __getitem__(self, item):
        a,b = 1,1
        for x in range(item):
            a,b = b,a+b
        return a

#list的切片方法

#__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice

class FibV3(object):
    def __getitem__(self, item):
        if isinstance(item,int):
            a,b = 1,1
            for x in range(item):
                a,b = b,a+b
            return a
        if isinstance(item,slice):
            start = item.start
            end = item.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(end):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L

'''
果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，
用于删除某个元素。
定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口
'''

#__getattr__

'''
正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错.要避免这个错误,，Python还有一个机制，
那就是写一个__getattr__()方法，动态返回一个属性
'''

class Student(object):
    def __init__(self):
        self.name = "wanghao"
    def __getattr__(self, item):
        if item == 'age':
            return 23

#注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。


#__call__

'''
一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在
实例本身上调用呢？在Python中，答案是肯定的。

任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
'''

class Person(object):
    def __init__(self,name):
        self.name = name
    def __call__(self, *args, **kwargs):
        print('my name is %s'%self.name)


#判断一个对象是否能被调用，能被调用的对象就是一个Callable对象

p = Person('wanghao')
callable(p)