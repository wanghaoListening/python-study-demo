
"""
字符串的操作方法练习
"""

def main():
    str1 = "hello world"
    #计算字符串长度
    print(len(str1))
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())
    # 获得字符串变大写后的拷贝
    print(str1.upper())
    # 从字符串中查找子串所在位置
    print(str1.find('or'))
    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('he'))
    # 检查字符串是否以指定的字符串结尾
    print(str1.endswith('ld'))
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, ' '))
    str2 = 'abcde1234'
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])  # c
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:6])
    # 检查字符串是否由数字构成
    print(str2.isdigit())
    # 检查字符串是否以字母构成
    print(str2.isalpha())
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())
    str3 = '  mike '
    print(str3)
    # 获得字符串修剪左右两侧空格的拷贝
    print(str3.strip())


if __name__ == '__main__':
    main()
