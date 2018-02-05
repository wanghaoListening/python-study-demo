
#动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的

class Gift(object):
    print('gift ...')

gift = Gift()

type(gift)
type(Gift)

'''
type()函数可以查看一个类型或变量的类型,gift:<class '__main__.Gift'>,Gift:<class 'type'>
type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Gift类

'''

'''
要创建一个class对象，type()函数依次传入3个参数：

1.class的名称；
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3.class的方法名称与函数绑定，这里我们把函数greet绑定到方法名hello上:
'''

def greet(self,name='boy'):
    print('hello %s'%(name))


Hello = type('Hello',(object,),dict(greet=greet))

h = Hello()

h.greet()

'''
通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常
大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
'''

