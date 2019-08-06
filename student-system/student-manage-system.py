

user_info = []

# 定义功能界面

def info_print():
    print('请选择功能--------------')
    print('1,添加学员')
    print('2,删除学员')
    print('3,修改学员')
    print('4,查询学员')
    print('5,显示所有学员')
    print('6 退出系统')
    print('-'*20)


# 添加用户
def add_info():
    """
    添加用户
    :return:
    """
    new_id = input('输入用户id')
    new_name = input('输入用户姓名')
    new_tel = input('输入用户手机号')

    for user in user_info:
        if new_name == user['name']:
            print(f'用户名{new_name}以及存在')
            return

    user_dict = {}

    user_dict['id'] = new_id
    user_dict['name'] = new_name
    user_dict['tel'] = new_tel
    user_info.append(user_dict)


while True:
# 1.显示功能界面
    info_print()

# 2.用户输入功能序号
    user_num = int(input('请选择序号'))

# 3.按照用户输入的功能序号，执行不同的功能
    if 1 == user_num:
        pass
    elif 2 == user_num:
        pass
    elif 3 == user_num:
        pass
    elif 4 == user_num:
        pass
    elif 5 == user_num:
        pass
    elif 6 == user_num:
        pass
    else:
        print('输入有误')

