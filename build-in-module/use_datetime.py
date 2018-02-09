
#datetime是Python处理日期和时间的标准库。

#获取当前日期时间

from datetime import datetime, timezone

now = datetime.now() #获取当前的datetime
print(now) #2018-02-09 10:34:37.946957
print(type(now))

dt = datetime(2015,4,19,12,20) # 用指定日期时间创建datetime
print(dt) #2018-01-20 12:20:00


#把一个datetime类型转换为timestamp只需要简单调用timestamp()方法

dt = datetime(2018,1,20,10,22)
print(dt.timestamp()) #1516422000.0

#注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。

#把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法
t = 1516422000.0
print(datetime.fromtimestamp(t))

'''
注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。
'''

#timestamp也可以直接被转换到UTC标准时区的时间

print(datetime.utcfromtimestamp(t))  # UTC时间

#str转换为datetime

cday = datetime.strptime('2018-1-1 10:20:20','%Y-%m-%d %H:%M:%S')
print(cday)

#datetime转换为str
now_time = datetime.now()
print(now_time.strftime('%Y-%m-%d %H:%M:%S'))

#datetime加减
#对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类

from datetime import datetime,timedelta,timezone

present_time = datetime.now()
print(present_time + timedelta(hours=10))
print(present_time - timedelta(days=1))
print(present_time + timedelta(days=2,hours=2))

#时区转换

#可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

# astimezone()将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))

'''
datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
'''