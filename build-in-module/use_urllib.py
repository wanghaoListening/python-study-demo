

#urllib提供了一系列用于操作URL的功能


from urllib import request

with request.urlopen('https://www.douban.com/') as f:
    data = f.read()
    print('status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s : %s'%(k,v))
    print('data:',data.decode('utf-8'))

'''
模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。
'''

req = request.Request('https:www.baidu.com')
req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36')
with request.urlopen(req) as f:
    print('status,',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s %s'%(k,v))
    print('data',f.read().decode('utf-8'))

'''
如果要以POST发送一个请求，只需要把参数data以bytes形式传入
如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
'''


