
#拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法

#我们来判断对象类型，使用type()函数


print(type(123)==int)

print(type('hello')==str)

#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数,使用types模块中定义的常量

import types

def fun():
    pass

print(type(fun) == types.FunctionType)

print(type(lambda x:x) == types.LambdaType)

print(type(abs) == types.BuiltinFunctionType)

#isinstance()就可以告诉我们，一个对象是否是某种类型

print(isinstance('123',str))
print(isinstance(123,int))


#要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list

#查看str的所有属性
dir(str)

'''
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
它自动去调用该对象的__len__()方法
'''

#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法


class House(object):
    def __len__(self):
        return 100


house = House()

len(house)

#仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态


class Person(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        self.location = 'china'
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name


person = Person('wanghao',23)

hasattr(person,'__name')

getattr(person,'__age')
getattr(person,'location')
getattr(person,'get_age')

#需要注意，getattr()、setattr()以及hasattr()只能操作public属性方法


