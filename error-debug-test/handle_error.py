
'''
Python作为高级语言通常都内置了一套try...except...finally...错误处理机制
'''

try:
    print('try...')
    r = 10/int('2')
    print('result:',r)
except ValueError as e:
    print('ValueError',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError',e)
finally:
    print('finally')

'''
Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
类似于java的Exception
常规的继承关系https://docs.python.org/3/library/exceptions.html#exception-hierarchy
'''
#注意:如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出

#记录错误
'''
如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，
然后分析错误原因，同时，让程序继续执行下去。
Python内置的logging模块可以非常容易地记录错误信息,通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
'''

import logging

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except BaseException as e:
        logging.exception(e)

main()
print('End')

#抛出错误
'''
首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
'''

class FooError(ValueError):
    pass

def testFoo(s):
    n  = int(s)
    if n == 0:
        raise FooError('invalid value %s'%s)
    return 10/n



