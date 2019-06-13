import pymysql
from  pymysql.cursors import DictCursor

"""
分页查询员工信息。
"""

class Emp(object):

    def __init__(self,no,name,job,sal):
        self.no = no
        self.name = name
        self.job = job
        self.sal = sal

    def __str__(self):
        return f'\n编号：{self.no}\n姓名：{self.name}\n职位：{self.job}\n月薪：{self.sal}\n'




def main():
    page = int(input('页码'))
    size = int(input('大小'))

    conn = pymysql.connect(host='localhost', port=3306,
                           database='python_demo', charset='utf8',
                           user='root', password='wh6532140')

    try:
        with conn.cursor() as cursor:
            cursor.execute('select eno as no, ename as name, job, sal from tb_emp limit %s,%s',((page - 1) * size, size))

            for emp_tuple in cursor.fetchall():
                print(emp_tuple)
                #参数，元组解包
                emp = Emp(*emp_tuple)
                print(emp)

    finally:
        conn.close()



if __name__ == '__main__':
    main()



