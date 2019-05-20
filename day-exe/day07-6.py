"""

和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类
相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类
相关的信息并且可以创建出类的对象
"""

from time import time,localtime,sleep


class Clock(object):

    def __init__(self,hour,minute,second):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)


    def run(self):

        self._second +=1
        if self._second >=60:
            self._second = 0
            self._minute +=1
            if self._minute >=60:
                self._minute = 0
                self._hour +=1
                if self._hour >=24:
                    self._hour = 0

    def show(self):
        print('%s:%s:%s' %(self._hour,self._minute,self._second))




def main():
    # 通过类方法创建对象并获取系统时间
    now = Clock.now()
    while True:
        now.show()
        sleep(1)
        now.run()



if __name__ == '__main__':
    main()


