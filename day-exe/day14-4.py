"""

实现线程安全的单利
"""


from functools import wraps


def singleton(cls):

    instance = {}

