
#类属性和实例属性

#实例属性，给实例绑定属性的方法是通过实例变量，或者通过self变量

class Student(object):

    def __init__(self,name):
        self.name = name



student = Student('wanghao')
student.age = 23


#类属性

class StudentV2(object):
    name = 'wanghao'
    def __init__(self):
        pass





'''
实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
'''