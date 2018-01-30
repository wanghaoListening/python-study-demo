
#继承，多态

class Animal(object):
    def run(self):
        print('Animal is running ... ...')

class Dog(Animal):
    def eat(self):
        print('eat meal')
    def run(self):
        print('dog is runing ....')

class Cat(Animal):
    def run(self):
        print('cat is runing .....')

dog = Dog()
dog.run()

isinstance(dog, Animal)

#动态语言的鸭子类型特点
'''
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
'''

class Clock(object):
    def run(self):
        print('时钟')



def run_fast(animal):
    animal.run()

run_fast(Dog())
run_fast(Cat())
run_fast(Clock())

