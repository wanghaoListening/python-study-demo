
#操作文件和目录

'''
Python内置的os模块也可以直接调用操作系统提供的接口函数
'''
import os

print(os.name) #操作系统类型,如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统

print(os.uname()) #取详细的系统信息

#操作系统中定义的环境变量，全部保存在os.environ这个变量中
print(os.environ)

#获取某个环境变量的值
os.environ.get('PATH')

#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中

#获取当前目录的绝对路径
os.path.abspath('.')

#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/home/wang','example01')

#创建一个目录
os.mkdir('/home/wang/example02')

os.remove('/home/wang/example02')

#两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
os.path.join('/home/wang/','example03')

#要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
os.path.split('.')
os.path.splitext('/home/wang/example02/le.py')
#shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
import shutil

shutil.copyfile('/home/wang/example1','/home/wang/example2')
#列出所有的.py文件

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
