
"""
python中创建类和对象
"""

"""
在Python中可以使用class关键字定义类，然后在类中通过之前学习过的函数来定义方法，这样就可以将对象的动态特征描述出来
"""

class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course):
        print('%s正在学习%s' % (self.name,course))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_tv(self):
        if self.age > 18:
            print("已经成年")
        else:
            print("未成年不能看电视")


"""
创建和使用对象
"""

def main():
    student = Student('xiaoming',25)
    student.study('python')
    student.watch_tv()

if __name__ == '__main__':
    main()
