#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'wanghao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

'''
导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。

sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，
例如：
运行python3 code_template.py获得的sys.argv就是['code_template.py']；

运行python3 code_template.py wang获得的sys.argv就是['code_template.py','wang']。
'''

