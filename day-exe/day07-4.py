
"""
我们讲到这里，不知道大家是否已经意识到，Python是一门动态语言。通常，动态语言允许我们在程序运行时给对象绑
定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定。但是如果我们需要限定自定义类型的对象只能绑定
某些属性，可以通过在类中定义__slots__变量来进行限定。需要注意的是__slots__的限定只对当前类的对象生效，对
子类并不起任何作用。
"""


class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name','_age','_gender')

    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name;


    def play(self):
        if self._age <18:
            print('%s未成年' %self._name)
        else:
            print('%s成年了，任意玩' %self._name)



def main():
    person = Person('lili',16)
    person.play()
    person._gender = 'female'
    print(person._gender)


if __name__ == '__main__':
    main()
