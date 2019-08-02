

#!/usr/bin/env python

# coding=utf-8

def main():
    numOfGroup = int(input())
    groups = []
    for index in range(numOfGroup):
        n = int(input())
        sequence_line = input()
        sequence_char = sequence_line.split(' ')
        numbers = [int(x) for x in sequence_char]
        query_count = int(input())
        ranges = []
        for j in range(query_count):
            rangeLine = input()
            rangeNt = rangeLine.split(' ')
            ranges.append(IRange(int(rangeNt[0]), int(rangeNt[1]), numbers))
        groups.append(Group(ranges))

    for j in range(numOfGroup):
        print("Case #"+str(j+1))
        group = groups[j]
        for pi in group.ranges:
            print(pi.sum)



class IRange(object):

    def __init__(self,start,end,sequences):
        self.start = start
        self.end = end
        nt = 1
        sum = 0
        for i in range(start - 1, end):
            sum += sequences[i] * nt
            nt += 1
        self.sum = sum


class Group(object):

    def __init__(self,ranges):
        self.ranges = ranges







if __name__ == '__main__':
    main()







