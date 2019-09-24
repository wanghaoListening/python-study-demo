
"""
走楼梯
"""



def jumpStep():
    n = int(input())
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    step1 = 1
    step2 = 2
    step3 = 4
    result = 0
    for i in range(4,n+1):
        result = (step1 + step2 + step3)%1000000007
        step1 = step2
        step2 = step3
        step3 = result
    print(result)


if __name__ == '__main__':
    result = jumpStep()
    print(result)
