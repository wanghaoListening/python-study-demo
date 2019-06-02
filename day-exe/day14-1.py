
"""
装饰器

输出函数执行时间的装饰器。
"""

from time import time

from functools import wraps


def record_time(func):
    """
    自定义装饰函数的装饰器
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time()
        result = func(*args,**kwargs)
        print(f'{func.__name__}:{time()-start}')
        return result
    return wrapper


