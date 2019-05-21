
"""
刚才我们提到了，可以在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，
从而减少重复代码的编写。提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或
衍生类。子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，在实际
开发中，我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，对应的原则称之为里氏替换原则。
"""


class Person(object):

    def __init__(self,name,age):
        self._name = name
        self._age = age


    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def age(self,age):
        self._age = age

    @name.setter
    def name(self,name):
        self._name = name

    def play(self):
        print('%s正在愉快的玩耍' %self._name)



class Student(Person):

    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,grade):
        self._grade = grade

    def study(self,course):
        print('%s正在学习%s' %(self._name,course))


class Teacher(Person):

    def __init__(self,name,age,title):
        super().__init__(name,age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        self._title = title

    def tech(self,course):
        print('%s正在教%s课程' %(self._name,course))




def main():

    student = Student('阿乐',21,30)
    student.study('python课程')
    student.play()

    teacher = Teacher('周老师',32,'教授')
    teacher.tech('python课程')
    teacher.play()



if __name__ == '__main__':
    main()