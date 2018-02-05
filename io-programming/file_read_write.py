
'''
操作IO的能力都是由操作系统提供的，每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用，Python也不例外
'''

import logging

logging.basicConfig(level=logging.INFO)

f = None
try:
    f = open('/home/wang/examples.desktop','r')
    print(f.read())
except IOError as e:
    logging.info("the error ex {}",e)
finally:
        f.close()


with open('/home/wang/examples.desktop','r') as f:
    print(f.read())


with open('/home/wang/examples.desktop','r') as f:
    for line in f.readlines():
        print(line.strip()+"end") ## 把末尾的'\n'删掉

'''
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用
read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，
调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文
件，调用readlines()最方便：
'''

#file-like Object

'''
像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可
以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
'''

#二进制文件
#前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可

f = open("/home/wang/le.jpg",'rb')
f.read()

#字符编码
#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件

f = open('/home/wang/example.txt','r',encoding='gbk')

'''
遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如
果遇到编码错误后如何处理。最简单的方式是直接忽略：
'''
f = open('/home/wang/example.txt','r',encoding='gbk',errors='ignore')

#写文件

#写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件

w = open('/home/wang/example.txt','w')
w.write('hello world')
w.close()

'''
以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入
'''



