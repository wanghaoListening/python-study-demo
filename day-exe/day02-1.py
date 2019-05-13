"""
用户身份验证
"""

username = input("输入用户名")
password = input("输入密码")

if username == 'admin' and password =='admin123':
    print("输入成功")

else:
    print("用户名或者密码失败")