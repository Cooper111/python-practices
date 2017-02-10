#
# Selection Sort
# First, find the smallest item in the array and exchange it with the first entry.
# Then, find the next smallest item and exchange it with the second entry.
# Continue this way until the entire array is sorted.
#


def exchange(mylist, a, b):
    if a == b:
        return
    temp = mylist[a]
    mylist[a] = mylist[b]
    mylist[b] = temp

def selectionSort(mylist):
    n = len(mylist)
    for i in range(0, n):
        cur = i
        minindex = cur
        for j in range(cur, n):
            if mylist[j] < mylist[minindex]:
                minindex = j
        exchange(mylist, cur, minindex)
    return mylist

def main():
    mylist = [8, 1, 9, 3, 6, 2, 4, 5]
    sortedlist = selectionSort(mylist)
    print(sortedlist)

if __name__ == "__main__":
    main()
