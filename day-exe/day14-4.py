"""

实现线程安全的单利
"""


from functools import wraps
import threading




def singleton(cls):

    instance = {}
    lock = threading.Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            with lock:
                if cls not in instance:
                    instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper



