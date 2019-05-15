
"""
实现了对列表的排序操作
"""

def main():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    print(list2)
    list3 = sorted(list1,reverse=True)
    print(list3)
    list4 = sorted(list1,key=len)
    print(list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)


if __name__ == "__main__":
    main()


