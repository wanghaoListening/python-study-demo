"""
使用列表
"""


def main():
    list1 = [1,2,3,4,5,6,7]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    # 计算列表长度(元素个数)
    print(len(list2))
    # 下标索引
    print(list2[2])
    print(list2[-2])
    #添加元素
    list1.append(100)
    #指定索引位置插入元素
    list1.insert(0,300)
    list1 += [10000,20000]
    print(list1)
    print(len(list1))
    # 删除元素
    list1.remove(2)
    if 345 in list1:
        list1.remove(345)

    del list1[1]

    print(list1)
    list1.clear()
    print(list1)



if __name__ == '__main__':
    main()









if __name__== '__main__':
    main()