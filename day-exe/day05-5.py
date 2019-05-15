"""
使用列表的生成式语法来创建列表
"""
import sys

def main():
    f = [x for x in range(1,10)]
    print(f)
    f = [x+y for x in "abcdef" for y in "123456"]
    print(f)
    #用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x**2 for x in range(1,20)]
    #查看对象占用的内存字节数
    print(sys.getsizeof(f))
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x**2 for x in range(1,30))
    print(sys.getsizeof(f))
    print(f)
    for val in f:
        print(val)

"""
除了上面提到的生成器语法，Python中还有另外一种定义生成器的方式，就是通过yield关键字将一个普通函数改造成生成器函数。
"""

if __name__ == '__main__':
    main()