#
# Shell Sort
# Based on insertion sort
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
        increment = int(increment/2)
        
        for i in range(0, n):
            cur = i
            for j in range(cur, 0, -increment):
                if mylist[j] > mylist[j-increment]:
                    exchange(mylist, j, j-increment)
    return mylist

def main():
    mylist = [8, 1, 9, 3, 6, 2, 4, 5]
    sortedlist = shellSort(mylist)
    print(sortedlist)

if __name__ == "__main__":
    main()
