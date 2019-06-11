import pymysql
from  pymysql.cursors import DictCursor


class Emp(object):

    def __init__(self,no,name,job,sal):
        self.no = no
        self.name = name
        self.job = job
        self.sal = sal

    def __str__(self):
        return f'\n编号：{self.no}\n姓名：{self.name}\n职位：{self.job}\n月薪：{self.sal}\n'






