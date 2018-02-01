
#给实例绑定一个方法

class Student(object):
    pass


s = Student()

def set_age(self,age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

#给一个实例绑定方法，对另一个实例不起作用，为了给所有实例都绑定方法，可以给class绑定方法

'''
如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
'''

class Person(object):
    __slots__ = ('name','age')

p = Person()
p.name = 'wanghao'
p.age = 23

'''
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
'''


