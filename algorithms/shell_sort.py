#
# Shell Sort
# Based on insertion sort, see Selection_sort.py
#

import math

def exchange(mylist, a, b):
    if a == b:
        return
    temp = mylist[a]
    mylist[a] = mylist[b]
    mylist[b] = temp

def shellSort(mylist):
    n = len(mylist)
    increment = n
    while increment > 1:
        increment = int(increment / 2)
        for i in range(0, n):
            cur = i
            for j in range(cur, 0, -increment):
                if mylist[j] > mylist[j-increment]:
                    exchange(mylist, j, j-increment)
    return mylist

def shellSort2(mylist):
    n = len(mylist)
    increment = n
    while increment > 1:
        increment = int(increment / 2)
        for i in range(0, n):
            cur = i
            j = cur
            while j > 0 and mylist[j] > mylist[j-1]:
                exchange(mylist, j, j-1)
                j -= 1
    return mylist

def shellSort3(mylist):
    n = len(mylist)
    increment = n
    while increment > 1:
        increment = int(increment / 2)
        for cursor in range(0, n):
            tmp = mylist[cursor]
            j = cursor
            while mylist[j] > tmp and j > 0:
                mylist[j] = mylist[j-1]
                j -= 1
            mylist[j] = tmp
    return mylist

def main():
    mylist = [8, 1, 9, 3, 6, 2, 4, 5]
    sortedlist = shellSort(mylist)
    print(sortedlist)
    sortedlist = shellSort2(mylist)
    print(sortedlist)
    sortedlist = shellSort3(mylist)
    print(sortedlist)
if __name__ == "__main__":
    main()
