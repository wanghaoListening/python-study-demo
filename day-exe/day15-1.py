
"""
插入一个部门
"""
import pymysql



def main():

    no = int(input('输入no'))
    name = input('输入名字')
    loc = input('所在地')

    conn = pymysql.connect(host='localhost', port=3306,
                          database='python_demo', charset='utf8',
                          user='root', password='wh6532140')

    try:
        with conn.cursor() as cursor:
            result = cursor.execute('insert into tb_dept values (%s, %s, %s)',(no,name,loc))
            if result == 1:
                print('插入数据成功')

            conn.commit()

    finally:
        conn.close()


if __name__ == '__main__':
    main()