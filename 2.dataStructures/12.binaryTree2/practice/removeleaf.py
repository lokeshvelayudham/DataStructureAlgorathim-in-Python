from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
import queue

# class for binary

class binaryTree :
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None

def removeLeaf(root):
    if root is None :
        return None
    if (root.left) is None and (root.right) is None :
        return None
    root.left = removeLeaf(root.left)
    root.right = removeLeaf(root.right)
    return root


# pritn binasrt tree
def printTree(root):
    if root == None :
        return
    print(root.data, end=":")

    if root.left != None:
        print("L",root.left.data,end=",")

    if root.right != None :
        print("R",root.right.data,end=" ")

    print()
    printTree(root.left)
    printTree(root.right)
# take input  
#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    root = binaryTree(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = binaryTree(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = binaryTree(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

# main
root = takeInput()
printTree(root)
removeLeaf(root)
printTree(root)

