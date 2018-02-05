

#很多时候，数据读写不一定是文件，也可以在内存中读写

#StringIO顾名思义就是在内存中读写str

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world !')
print(f.getvalue())#获得写入后的str

#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO

from io import BytesIO

b = BytesIO()
b.write('中国'.encode('utf-8'))
print(b.getvalue())

#StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口