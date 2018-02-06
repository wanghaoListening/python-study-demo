
import json


class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bod',20,90)

print(json.dumps(s,default=lambda obj:obj.__dict__))
str = json.dumps(s,default=lambda obj:obj.__dict__)

#通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

'''
同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，
我们传入的object_hook函数负责把dict转换为Student实例
'''

def dictstudent(d):
    return Student(d['name'],d['age'],d['score'])

print(json.loads(str,object_hook=dictstudent))