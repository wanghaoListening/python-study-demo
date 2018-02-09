
#Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等

import hashlib

md5 = hashlib.md5()
md5.update('I love china'.encode('utf-8'))
print(md5.hexdigest())

'''
如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
'''
md5_text = hashlib.md5()
md5_text.update('how to use md5'.encode('utf-8'))
md5_text.update('python hashlib?'.encode('utf-8'))
print(md5_text.hexdigest())

#SHA1摘要算法
'''
调用SHA1和调用MD5完全类似
'''
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

'''
SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
'''