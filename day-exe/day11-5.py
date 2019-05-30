"""
day11-4的客户端实现
"""

from socket import socket
from json import loads

from base64 import b64decode




def main():

    client = socket()
    client.connect(('127.0.0.1', 2288))
    # 定义一个保存二进制数据的对象
    print(client)
    in_data = bytes()
    data = client.recv(1024)
    print(data)
    while data:
        in_data +=data
        data = client.recv(1024)
    # 将收到的二进制数据解码成JSON字符串并转换成字典
    # loads函数的作用就是将JSON字符串转成字典对象
    print(len(in_data))
    my_dict = loads(in_data.decode('UTF-8'))
    filename = my_dict['filename']
    data = my_dict['data']

    with open('/Users/admin/'+filename,'wb') as f:
        f.write(b64decode(data))
    print('图片已经保存')


if __name__ == '__main__':
    main()