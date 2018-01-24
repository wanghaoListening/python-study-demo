
'''
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
'''
#生成1-10的列表
list(range(1,11))

#生成[1x1, 2x2, 3x3, ..., 10x10]
print([x*x for x in range(1,11)])

#for循环后面还可以加上if判断
print([x*x for x in range(1,11) if x%2 == 0])

#使用两层循环，可以生成全排列：
print([m+n for m in "abcd" for n in "efgh"])

#使用两个变量来生成list

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [v.lower() for v in L1 if isinstance(v,str)]