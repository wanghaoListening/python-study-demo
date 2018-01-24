
'''
如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
'''

#方法一，只要把一个列表生成式的[]改成()，就创建了一个generator,通过next()函数获得generator的下一个返回值

g = (x * x for x in range(10))

print(next(g))

#generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素


#方法二，如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1
    return "done"

#要把fib函数变成generator，只需要把print(b)改为yield b就

def fibV2(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return "done"

f = fibV2(10)
print(next(f))

for value in f:
    print(value)
'''
generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的
函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''

