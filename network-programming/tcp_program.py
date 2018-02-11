
import socket

#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.baidu.com',80))

'''
创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用
面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。
'''