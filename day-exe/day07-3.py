"""

之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，
但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效。
我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议
外界直接访问，那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）
方法进行对应的操作。如果要做到这点，就可以考虑使用@property包装器来包装getter和
setter方法，使得对属性的访问既安全又方便

利用@property来控制访问的权限
"""


class Person(object):

    def __init__(self,name,age):
        self._name = name
        self._age = age

    #访问器 - getter方法
    @property
    def name(self):
        return self._name

    #访问器 - getter方法
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age

    # 修改器 - setter方法
    def display(self):
        if self._age < 16:
            print('%s正在玩飞行棋' %self._name)
        else:
            print('%s正在学习' %self._name)


def main():
    person = Person('john',18)
    person.display()
    person.age = 13
    person.display()



if __name__ == '__main__':
    main()


