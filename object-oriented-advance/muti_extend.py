
#多重继承

class TCPServer(object):
    pass

class ForkingMixIn(object):
    pass


class MyTCPServer(TCPServer,ForkingMixIn):
    pass

'''
不同于java，python支持多继承，这样一来，我们不需要复杂而庞大的继承链，
只要选择组合不同的类的功能，就可以快速构造出所需的子类
'''