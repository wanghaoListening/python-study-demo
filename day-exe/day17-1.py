
import random


teachers = ['A','B','C','D','E','F','G','H']
offices = [[],[],[]]

for name in teachers:

    num = random.randint(0,2)
    offices[num].append(name)



for office in offices:

    print(f'办公室的人数为{len(office)}')
    print(f'办公室成员为{office}')


