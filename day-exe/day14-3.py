"""
用装饰器来实现单例模式。
"""

from functools import wraps

def singleton(cls):
    instance = {}

    @wraps(cls)
    def wrapper(*args,**kwargs):
        if cls not in instance:
            instance[cls] = cls(args,kwargs)
        return instance[cls]

    return wrapper



@singleton
class Preident():
    """
    总统单利
    """
    pass