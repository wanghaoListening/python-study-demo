
from threading import Thread
from json import dumps
from base64 import b64encode

from socket import socket,SOCK_STREAM, AF_INET






class FileTransferServer(Thread):

    def __init__(self,cclient,data):
        super().__init__()
        self.cclient = cclient
        self.data = data

    def run(self):
        my_dict = {}
        my_dict['filename'] = 'wanghao.jpg'
        # 所以图片的二进制数据要处理成base64编码
        my_dict['data'] = self.data
        # 通过dumps函数将字典处理成JSON字符串
        json_str = dumps(my_dict)
        # 发送json字符串
        self.cclient.send(json_str.encode('utf-8'))
        print('已发送字符串')
        self.cclient.close()



def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 2.绑定IP地址和端口(区分不同的服务)
    server.bind(('127.0.0.1', 5588))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器开始监听')
    with open('/Users/admin/Desktop/wanghao.jpg','rb') as file:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(file.read()).decode('utf-8')
        print('读取文件成功')
    while True:
        client,addr = server.accept()
        print('客户端'+str(addr)+'连接成功')
        # 启动一个线程来处理客户端请求
        FileTransferServer(client,data)


if __name__ == '__main__':
    main()

