

#位置参数

def power(x,n):
    s = 1
    while n >=1:
        s = s*x
        n = n-1
    return s


#默认参数,默认参数可以简化函数的调用

def powerv2(x,n=2):
    s = 1
    while n >=1:
        s = s*x
        n = n-1
    return s

def enroll(name,gender,age=6,city='beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age',age)
    print('city',city)


def add_end(L=None):
    if L is None:
        L = []
    L.append('End')
    return L;


'''
注意：
一是必选参数在前，默认参数在后，否则Python的解释器会报错
二是当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
Python函数在定义的时候，默认参数L的值就被计算出来了,定义默认参数要牢记一点：默认参数必须指向不变对象！
关于不变对象的好处？
为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于
修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在
编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
'''

#可变参数

def calc(*numbers):
    sum = 0
    for num in numbers:
        sum+=num
    return sum

print(calc(1,2,3,4,5,6,7))

numbers = (1,2,3,4,5,6,7)
#*nums表示把nums这个tuple的所有元素作为可变参数传进去
print(calc(*numbers))

#关键字参数

'''
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传
入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
'''

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)


person('wanghao','男')

person('wanghao','男',city='beijing',school='fanhua')

extra = {'city': 'Beijing', 'job': 'Engineer'}

person('wanghao','male',**extra)

'''
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
'''

#命名关键字参数

'''
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
'''

def personV2(name,age,*,city,job):
    print(name,age,city,job)

personV2('Jack', 24, city='Beijing', job='Engineer')

'''
如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
'''
def personV2(name, age, *args, city, job):
    print(name, age, args, city, job)


def personV3(name,age,*,city='beijing',job):
    print(name,age,city,job)

personV3('Jack', 24, job='Engineer')

#参数组合

'''
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''

def combinationV1(a,b,c=0,*args,**kwargs):
    print(a,b,c,args,kwargs)

def combinationV2(a,b,c=0,*,d,**kwargs):
    print(a,b,c,d,kwargs)

