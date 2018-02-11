
'''
在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。
顾名思义，psutil = process and system utilities，它不仅可以
通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等
'''

import psutil

psutil.cpu_count() #CPU逻辑数量
psutil.cpu_count(logical=False)# CPU物理核心

psutil.cpu_times() #统计CPU的用户／系统／空闲时间

psutil.virtual_memory() #使用psutil获取物理内存

psutil.disk_partitions() ## 磁盘分区信息

psutil.net_io_counters()# 获取网络读写字节／包的个数

psutil.net_connections() #获取当前网络连接信息

psutil.pids() # 所有进程ID