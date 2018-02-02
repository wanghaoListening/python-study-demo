
#枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：

from enum import Enum,unique

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)


#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
#@unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    SUN = 0
    MON = 1
    THE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6

sun = Weekday.SUN
print(sun)
print(sun.value)