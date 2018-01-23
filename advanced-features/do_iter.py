
from collections import Iterable

d = {'a':1,'b':2,'c':3,'d':4}

#默认dict的迭代，是迭代key
for key in d:
    print(key)

#若想迭代values
for value in d.values():
    print(value)

#迭代key与value
for key,value in d.items():
    print(key,value)

#字符串也是可迭代对象
for ch in "abcdefg":
    print(ch)

#判断一个对象是否是可迭代对象
print(isinstance('abc',Iterable))

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身

for i,value in enumerate(['A','B','C']):
    print(i,value)

#同时引用了两个变量，在Python里是很常见的
for i,j in [(1,2),(3,4),(5,6)]:
    print(i,j)