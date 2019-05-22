"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

from abc import ABCMeta,abstractmethod


class People(object,metaclass=ABCMeta):
    """

    """
    __slots__ = ('_name')

    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name


    @abstractmethod
    def salary(self):
        """
        薪水
        :return:
        """
        pass



class Manager(People):
    """
    经理
    """
    __slots__ = ('_name')

    def salary(self):
        return 15000.0


class Programmer(People):
    """
    程序员
    """
    def __init__(self,name,working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour


