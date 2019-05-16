
"""
使用集合
Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算
"""


def main():
    #集合默认会剔除重复元素并且进行排序
    set1 = {1,2,3,4,2,3,6,5}
    print(set1)
    print('lenth',len(set1))
    set2 = set(range(1,10))
    print(set2)
    set1.add(4)
    set1.add(7)
    print(set1)
    # 从集合删除5
    set2.discard(5)
    print(set2)
    #遍历集合容器
    for ele in set1:
        print(ele)

    # 将元组转换成集合
    set3 = set(set2)
    print(set3.pop())
    print(set3)
    # 集合的交集、并集、差集、对称差运算
    print(set1 & set2)
    # print(set1.intersection(set2))
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)
    # print(set1.symmetric_difference(set2))

    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))






if __name__ == '__main__':
    main()