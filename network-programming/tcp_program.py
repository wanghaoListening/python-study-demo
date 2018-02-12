
import socket

#客户端
#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.baidu.com',80))

'''
创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用
面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。
'''
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接收数据
buffer = []
while True:
    #每次最多接受1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

#把接受的数据返回到文件
with open('/home/wang/sina.html','wb') as f:
    f.write(html)

#关闭连接
s.close()

#服务端
import threading
import time
#创建一个基于IPv4和TCP协议的Socket
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(('127.0.0.1,8888'))
#传入的参数指定等待连接的最大数量
ss.listen(10)
print('waiting for connection ...')

#每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接
def tcplink(sock,addr):
    print('accept new connection from %s,%s'%addr)
    sock.send(b'welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection from %s:%s closed'%addr)

while True:
    #接受一个新连接
    sock,addr = s.accept()
    #创建新线程来处理客户端连接
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()








