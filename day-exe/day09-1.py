
"""
读取文本文件时，需要在使用open函数时指定好带路径的文件名（可以使用相对路径或绝对路径）并将文件模式设
置为'r'（如果不指定，默认值也是'r'），然后通过encoding参数指定编码（如果不指定，默认值是None，那么
在读取文件时使用的是操作系统默认的编码），如果不能保证保存文件时使用的编码方式与encoding参数指定的编
码方式是一致的，那么就可能因无法解码字符而导致读取失败
"""

import time

def read_text():
    f = open('/Users/admin/test.txt','r',encoding='UTF-8')
    print(f.read())
    f.close()

def read_text_except():
    f = None
    try:
       f = open('/Users/admin/test.txt','r',encoding='UTF-8')
       print(f.read())
    except FileNotFoundError:
        print('找不到文件异常')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件解码错误')
    finally:
        if f:
            f.close()


def read_text_with():
    f = None
    try:
        with open('/Users/admin/test.txt','r',encoding='UTF-8') as f:
              print(f.read())
    except FileNotFoundError:
        print('找不到文件异常')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件解码错误')



def read_text_with_line():
    with open('/Users/admin/test.txt','r',encoding='UTF-8') as f:
        for line in f:
            print(line,end= '')
            time.sleep(0.5)


def read_text_lines():
    with open('/Users/admin/test.txt', 'r', encoding='UTF-8') as f:
        print(f.readlines())


if __name__ == '__main__':
    read_text_lines()