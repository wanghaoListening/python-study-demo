"""
自定义带参数的装饰器
"""

from functools import wraps
from time import time


#如果装饰器不希望跟print函数耦合，可以编写带参数的装饰器。


def record(output):
    """
    自定义带参数的装饰器
    :param output:
    :return:
    """
    def decorate(func):

        @wraps(func)
        def wrapper(*args,**kwargs):
            start = time()
            result = func(*args,**kwargs)
            output(func.__name__,time()-start)
            return result
        return wrapper
    return decorate


