
'''
安装驱动
sudo pip3 install mysql-connector==2.1.6
'''



import mysql.connector

conn = mysql.connector.connect(user='root',password='root',database='ouyeel')
cursor = conn.cursor()
cursor.execute('select * from ouyeel_steel where id < %s',('10',))
values = cursor.fetchall()
print(values)

#关闭连接
cursor.close()
conn.close()

'''
执行INSERT等操作后要调用commit()提交事务；
MySQL的SQL占位符是%s。
'''
