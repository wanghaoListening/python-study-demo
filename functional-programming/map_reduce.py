

def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8])
list(r)

'''
map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序
列，因此通过list()函数让它把整个序列都计算出来并返回一个list
'''
from functools import reduce

def add(x,y):
    return x+y

reduce(add,[1,3,5,7,9])
'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把
结果继续和序列的下一个元素做累积计算
'''
def fn(x,y):
    return x*10+y

reduce(fn,[1,3,5,7,9])

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

#使用lambda进一步简化
def char2num(s):
    return DIGITS[s]

def strV2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
'''
def normalize(name):
    return str(name)[:1].upper()+str(name)[1:len(name)].lower()

list(map(normalize,['adam', 'LISA', 'barT']))