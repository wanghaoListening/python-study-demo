"""
更新一个部门
"""

import pymysql


def main():

    no = int(input('输入编号'))
    name = input('输入名称')

    conn = pymysql.connect(host='localhost', port=3306,
                           database='python_demo', charset='utf8',
                           user='root', password='wh6532140')
    try:

        with conn.cursor() as cursor:

            result = cursor.execute('update tb_dept set dname=%s where dno=%s',(name,no))
            if result == 1:
                print('更新记录成功')
                conn.commit()
    finally:
        conn.close()




if __name__ == '__main__':
    main()
