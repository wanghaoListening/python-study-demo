
'''
Python内置的sorted()函数就可以对list进行排序
sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
'''
sorted([36, 5, -12, 9, -21])

sorted([36, 5, -12, 9, -21], key=abs)

#字符串忽略大小写，按照字母序排序。要实现这个算法

sorted(["acdnew","ASdwokec","dwnwwu","dfwGR","REWCXH"],key=str.lower)

#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True

sorted([3,45,213,543,12,54,11,2434,2,],reverse=True)

#练习，对列表按名字排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]



