
class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s, %s' %(self.name,self.score))

    def get_grade(self):
        if self.score > 90:
            print('A')
        elif self.score > 80:
            print('B')
        else:
            print('C')

bart = Student('wanghao', 23)
bart.print_score()
bart.get_grade()

'''
特殊方法“__init__”前后分别有两个下划线
和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
'''

#数据封装
#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个
# 类的不同实例，但拥有的变量名称都可能不同

bart.age = 10
print(bart.age)
