
"""
Python提供了re模块来支持正则表达式相关操作
"""

"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""

import re


def main():
    username = input('请输入正确的用户名')
    qq = input('请输入正确的qq号')

    username_match = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)

    if not username_match:
        print('请输入正确的用户名')
    qq_match = re.match(r'^[1-9]\d{4,11}$',qq)
    if not qq_match:
        print('请输入正确的qq号')
    if username_match and qq_match:
        print('您输入的正确:验证通过')



if __name__ == '__main__':
    main()
