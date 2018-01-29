
#函数作为返回值

#返回求和的函数

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax+n
        return ax
    return sum

m = lazy_sum(1,2,3,4,5,7)
#当调用m时才是真正的求和计算
m()

'''
我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变
量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）
注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数
'''

#注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用


#闭包

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()

#f1(),f2(),f3()都是９
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

#注意：返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。







