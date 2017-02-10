#
# Insertion Sort
#

def exchange(mylist, a, b):
    if a == b:
        return
    temp = mylist[a]
    mylist[a] = mylist[b]
    mylist[b] = temp

def insertionSort(mylist):
    n = len(mylist)
    for i in range(0, n):
        cur = i
        for j in range(cur, 0, -1):
            if mylist[j] > mylist[j-1]:
                exchange(mylist, j, j-1)
    return mylist

# A better solution
def insertionSort2(mylist):
    n = len(mylist)
    for i in range(0, n):
        cur = i
        j = cur
        while j > 0 and mylist[j] > mylist[j-1]:
            exchange(mylist, j, j-1)
            j -= 1
    return mylist

# Without the exchange() method
def insertionSort3(mylist):
    n = len(mylist)
    for i in range(0, n):
        cur = i
        j = cur
        tmp = mylist[cur]
        while j > 0 and tmp > mylist[j-1]:
            mylist[j] = mylist[j-1]
            j -= 1
        mylist[j] = tmp

    return mylist


def main():
    mylist = [8, 1, 9, 3, 6, 2, 4, 5]
    sortedlist = insertionSort3(mylist)
    print(sortedlist)

if __name__ == "__main__":
    main()
