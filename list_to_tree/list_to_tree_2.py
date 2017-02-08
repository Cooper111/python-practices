#
# 问题：将一个排序好的数组转化成一个搜索二叉树?
# list_to_tree.py 将排序好的数组转化成适合二叉树的数组的方法的更好的思路。
#

import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def put(self, x, value):

        if x == None:
            return Node(value)

        if value < x.value:
            x.left = self.put(x.left, value)
        elif value > x.value:
            x.right = self.put(x.right, value)
        else:
            x.value = value

    def putItem(self, value):
        self.root = self.put(self.root, value)



def list_to_treelist(list):
    newList = []
    startCursor = 0
    endCursor = len(list) - 1
    b = True

    for _ in range(0, len(list)):
        if b:
            newList.insert(0, list[startCursor])
            startCursor += 1
        else:
            newList.insert(0, list[endCursor])
            endCursor -= 1
        b = not b

    return newList

def main():
    if __name__ == "__main__":
        myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        treeList = list_to_treelist(myList)
        print(treeList)
        tree = Tree()
        for i in range(0, len(treeList) - 1):
            value = treeList[i]
            print(value)
            tree.putItem(value)

main()
