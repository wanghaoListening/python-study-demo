"""
python 属性访问权限问题
在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头

在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。所以大多数Python程序员会遵循一种命名惯
例就是让属性名以单下划线开头来表示属性是受保护的，本类之外的代码在访问这样的属性时应该要保持慎重。这种做法并不是语法上的规则，
单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻

"""
import time

class Clock(object):

    def __init__(self,hour=0,minute=0,second=0):
        """

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second


    def run(self):
        self._second +=1
        if self._second >=60:
            self._second = 0
            self._minute += 1
            if self._minute >=60:
                self._minute = 0
                self._hour +=1
                if self._hour >=24:
                    self._hour = 0


    def show(self):
        return '%02d:%02d:%02d' %(self._hour,self._minute,self._second)



def main():

    clock = Clock(23,10,11)
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()



if __name__ == '__main__':
    main()



