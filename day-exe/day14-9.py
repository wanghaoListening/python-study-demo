"""
多线程程序如果没有竞争资源处理起来通常也比较简单
当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
说明：临界资源就是被多个线程竞争的资源
"""

import time
import threading

from concurrent.futures import ThreadPoolExecutor

class Account(object):
    """银行账号"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()


    def deposit(self,money):
        # 通过锁保护临界资源
        with self.lock:
            self.balance = self.balance + money



class AddMoneyThread(threading.Thread):
    """自定义线程类"""

    def __init(self,account,money):
        self.account = account
        self.money = money
        #自定义线程类必须调用父类的初始化方法
        super().__init__()

    def run(self):
        # 线程启动之后要执行的操作
        self.account.deposit(self.money)





def main():
    account = Account()
    #创建线程池
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for _ in range(100):
        # 创建线程的第1种方式
        # threading.Thread(
        #     target=account.deposit, args=(1, )
        # ).start()
        # 创建线程的第2种方式
        # AddMoneyThread(account, 1).start()
        # 创建线程的第3种方式
        # 调用线程池中的线程来执行特定的任务
        future = pool.submit(account.deposit,1)
        futures.append(future)

    pool.shutdown()
    for future in  futures:
        future.result()
    print(account.balance)


if __name__ == '__main__':
    main()




