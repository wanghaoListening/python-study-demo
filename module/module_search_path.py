
import sys
#当我们试图加载一个模块时，Python会在指定的路径下搜索对应的sys.py文件

#默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
print(sys.path)

#添加自己的模块,这种方法是在运行时修改，运行结束后失效。

sys.path.append('/home/wang/python_script')

'''
第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。
'''
