
'''
WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求
'''

def application(environ,start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return [b'<h1>Hello, web!</h1>']



# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()