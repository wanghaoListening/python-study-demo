"""
Python中的json模块
"""

import json

def write_json():
    mydict = {
        'name': 'wanghao',
        'age': 25,
        'qq': 9834755,
        'friends': ['wangpeng', 'ali'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        with open('/Users/admin/wang.json','w',encoding='UTF-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('保存个人信息完成')



def read_json():
    try:
        with open('/Users/admin/wang.json', 'r', encoding='UTF-8') as fs:
            person = json.load(fs)
            print(person)
    except IOError as e:
        print(e)



if __name__ == '__main__':
    read_json()

