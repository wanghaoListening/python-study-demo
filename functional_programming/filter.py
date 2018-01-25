
'''
filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''

def is_odd(n):
    return n%2 == 1

list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))

#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

#求素数

def is_palindrome(n):
    num = str(n)
    num_size = len(num)
    index = 1
    #定义指针
    while index <= num_size/2:
        if num[:index] == num[-index:]:
            index = index+1
            continue
        else:
            return False
    return True

list(filter(is_palindrome, range(1,100)))