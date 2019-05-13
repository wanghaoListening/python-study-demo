"""
输入一个正整数判断它是不是素数
"""

from math import sqrt

num = int(input("输入一个整数"))
end = int(sqrt(num))

flag = True
for i in range(2,end+1):
    if num % i == 0:
        flag = False
        break

if flag and num !=1:
    print("是个素数")
else:
    print("不是素数")
