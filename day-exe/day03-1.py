"""
用for循环实现1~100之间的偶数求和
"""

sum = 0
for unit in range(2,102,2):
    sum=sum+unit
print('和为：',sum)