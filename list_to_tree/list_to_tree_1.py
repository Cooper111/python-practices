#
# 问题：将一个排序好的数组转化成一个搜索二叉树？
# 思路：二叉树最好情况下是一棵平衡二叉树，所以，从已排序的数组的中间位置开始往两边取数据进行构建二叉树。
# 所以第一步是将排序好的数组转换顺序，从中间开始往外取数的顺序，例如，[1,2,3,4,5] -> [3,2,4,1,5]
# 思路不对，正确思路查看 list_to_tree_3.py
#

import sys

def getMiddleIndex(n):
    if n % 2 == 1:
        return int((n - 1) / 2)
    else:
        return int(n / 2)

middleIndex = -1
prevIndex = -1
nextIndex = -1
b = False
def getNextIndex(n):
    global middleIndex
    global prevCursorIndex
    global nextCursorIndex
    global b
    if middleIndex == -1:
        middleIndex = getMiddleIndex(n)
        prevCursorIndex = middleIndex
        nextCursorIndex = middleIndex
        return middleIndex
    else:
        b = not b
        if b:
            prevCursorIndex = prevCursorIndex - 1
            return prevCursorIndex
        else:
            nextCursorIndex = nextCursorIndex + 1
            return nextCursorIndex

def list_to_treelist(myList):
    newList = []
    n = len(myList)
    index = 1
    for _ in range(0, n):
        item = myList[getNextIndex(n)]
        newList.append(item)
    return newList

def main():
    if __name__ == "__main__":
        myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        treeList = list_to_treelist(myList)
        print(treeList)

main()
