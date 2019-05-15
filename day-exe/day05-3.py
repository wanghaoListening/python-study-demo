

"""
列表也可以做切片操作，通过切片操作我们可以实现对列表的复制或者将列表中的一部分取出来创建出新的列表
"""

def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    for fruit in fruits:
        print(fruit.title())
    # 列表切片
    fruits2 = fruits[1:3]
    print(fruits2)
    fruits3 = fruits[:]
    print(fruits3)
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)



if __name__ == '__main__':
    main()