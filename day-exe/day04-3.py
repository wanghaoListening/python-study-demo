

def fun():
    global a
    a = 100
    print(a)



if __name__=='__main__':
    a = 30
    fun()
    print(a)