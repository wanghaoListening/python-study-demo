
"""
查询所有的部门
"""

import pymysql
from pymysql.cursors import DictCursor


def main():
    conn = pymysql.connect(host='localhost', port=3306,
                           database='python_demo', charset='utf8',
                           user='root', password='wh6532140')

    try:
        with conn.cursor(cursor=DictCursor) as cursor:
            cursor.execute('select dno as no, dname as name, dloc as loc from tb_dept')
            results = cursor.fetchall()
            print(results)
            print('编号\t名称\t\t所在地')

            for dept in results:
                print(dept['no'], end='\t')
                print(dept['name'], end='\t')
                print(dept['loc'])

    finally:
        conn.close()


if __name__ == '__main__':
    main()