"""
启动5个线程向账户中存钱，5个线程从账户中取钱，取钱时如果余额不足就暂停线程进行等待。为了达到上述目标，需
要对存钱和取钱的线程进行调度，在余额不足时取钱的线程暂停并释放锁，而存钱的线程将钱存入后要通知取钱的线程，
使其从暂停状态被唤醒。可以使用threading模块的Condition来实现线程调度，该对象也是基于锁来创建的

"""

"""
多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition
"""

from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading


class Account():
    """银行账户"""

    def __init__(self,balance=0):
        self.balance = balance
        lock = threading.Lock()
        self.condition = threading.Condition(lock)


    def withdraw(self,money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            sleep(0.01)
            self.balance = new_balance


    def deposit(self,money):
        """存钱"""

        with self.condition:
            new_balance = self.balance + money
            sleep(0.01)
            self.balance = new_balance
            self.condition.notify_all()



def add_money(account):
    money = randint(10,30)
    account.deposit(money)
    print(threading.current_thread().name,':',money,'======>',account.balance)
    sleep(0.05)


def sub_money(account):
    money = randint(5,10)
    account.withdraw(money)
    print(threading.current_thread().name,':',money,'=======>',account.balance)
    sleep(0.05)



def main():
    account = Account()
    with ThreadPoolExecutor(max_workers=20) as pool:
        for _ in range(5):
            pool.submit(add_money,account)
            pool.submit(sub_money,account)
    print("account",account.balance)



if __name__ == '__main__':
    main()