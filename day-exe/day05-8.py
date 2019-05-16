
"""
字典是另一种可变容器模型，类似于我们生活中使用的字典，它可以存储任意类型对象，与列表、集合不同的是，
字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开
"""

def main():
    scores = {"mike":90,"qiao":100,"james":76}
    print(scores['mike'])
    # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
    for ele in scores:
        print("%s---->%t",(ele,scores[ele]))

    # 更新字典中的元素
    scores['mike'] = 98
    scores.update(john=10,polo=70)
    print(scores)
    print(scores.get('qiao'))
    #删除字典中的元素
    print(scores.popitem())
    print(scores.pop('james'))
    print(scores)
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main();