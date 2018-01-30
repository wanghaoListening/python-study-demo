
#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）

#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：

int('12345')

#但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：

int('12345',base=2)

#假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：

import functools

int2 = functools.partial(int,base=2)

int2('1000000')

'''
所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
返回一个新的函数，调用这个新函数会更简单。
'''

