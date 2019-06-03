"""

月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""

from abc import ABCMeta,abstractmethod


class Employee(metaclass=ABCMeta):
    """
    员工抽象类
    """
    def __init__(self,name):
        self.name = name


    @abstractmethod
    def get_salary(self):
        '''月薪水'''
        pass




class Manager(Employee):


    """部门经理"""
    def get_salary(self):
        return 15000.0

class Programmer(Employee):

    """程序员"""
    def __init__(self,name,working_hour):
        super().__init__(name)
        self.working_hour = working_hour


    def get_salary(self):
        return self.working_hour*200



class Saler(Employee):

    """销售员"""
    def __init__(self,name,sale_money):
        super().__init__(name)
        self.name = name
        self.sale_money = sale_money

    def get_salary(self):
        return 1500+self.sale_money*0.05




class EmployeeFactory():
    """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""

    @staticmethod
    def create(emp_type,*args,**kwargs):
        """创建员工"""
        emp_type = emp_type.upper()
        emp = None

        if emp_type == 'M':
            emp =  Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp =  Saler(*args, **kwargs)
        else:
            return emp
        return emp



def main():
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        if emp != None:
            print('%s:薪水是%.2f' %(emp.name,emp.get_salary()))




if __name__ == '__main__':
    main()

