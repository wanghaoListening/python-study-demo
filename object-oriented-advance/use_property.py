
'''
在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
Python内置的@property装饰器就是负责把一个方法变成属性调用的
'''


class Student(object):
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
        if value <0 or value>100:
            raise ValueError('score must between 0-100')
        self.__score = value


s = Student()

s.score = 79

print(s.score)

#利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution

class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        self.__height = value
    @property
    def resolution(self):
        return self.__height * self.__width
