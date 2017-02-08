#
# 1. Construct a node for the middle element in the array and return it.
# 2. Repeat from 1. on the left half of the array, assigning the return value to the left child of the root.
# 3. Repeat from 1. on the right half of the array, assigning the return value to the right child of the root.
#

class Node:
    def __init__(self, value):
        self.value = value

def sortedListToBST(myList, start, end):
    if start > end:
        return None
    mid = int(start + (end - start) / 2)
    node = Node(myList[mid])
    node.left = sortedListToBST(myList, start, mid - 1)
    node.right = sortedListToBST(myList, mid + 1, end)
    return node

def buildBST(myList):
    return sortedListToBST(myList, 0, len(myList) - 1)

# display a binary search tree
def display(parentValue, str, node):
    if node != None:
        print(parentValue, str, node.value)
        display(node.value, "left:", node.left)
        display(node.value, "right:",node.right)

def main():
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    bst = buildBST(myList)
    display('root', '', bst)

if __name__ == "__main__":
    main()
