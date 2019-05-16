"""
设计一个函数返回给定文件名的后缀名。
"""


def get_suffix(filename,has_dot=False):
    """

    :param filename: 文件名
    :param has_dot: 是否带着标点
    :return: 文件名
    """
    pos = filename.rfind('.')
    if 0 < pos <len(filename):
        index = pos if has_dot else pos+1
        return filename[index:]
    else:
        return ''


if __name__ == '__main__':
    print(get_suffix('city.world',True))
