"""

通过Python的程序来实现TCP客户端的功能
"""

from socket import socket

def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    client = socket()
    # 2.连接到服务器(需要指定IP地址和端口)
    client.connect(('127.0.0.1',7789))
    # 3.从服务器端接收数据
    print(client.recv(1024).decode('UTF-8'))
    client.close()




if __name__ == '__main__':
    main()