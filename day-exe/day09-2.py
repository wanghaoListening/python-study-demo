"""
读写二进制文件
"""

def main():
    try:
        with open('/Users/admin/Downloads/数据结构常用算法数据结构算法.doc','rb') as fread:
            data = fread.read()
            print(type(data))
        with open('/Users/admin/sjjg.doc','wb') as fwrite:
            fwrite.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开')
    except IOError as e:
        print('读写文件出现错误')
    print('指定程序结束')


if __name__ == '__main__':
    main()