
import os



def test_md5():
    md5hash = getattr(__import__('hashlib'), 'md5')()
    print(dir(md5hash))



def test_rfind():
    file_path = '/mak/admin/le/re.txt'
    print(file_path.rfind('/'))


def test_split_text():
    print(os.path.splitext('/mak/admin/le/re.txt'))


if __name__ == '__main__':
    test_split_text()

