''' 
    Time Complexity : O(N)
    Space Complexity : O(N)

    Where 'N' is the number of nodes in the given binary search tree.
'''

from sys import stdin, setrecursionlimit
from queue import Queue
from collections import defaultdict
setrecursionlimit(10**7)

# Binary tree node class for reference.
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def applyReverseInOrder(root, sum):

    if (root == None):
        return sum

    # Go to the right subtree.
    sum = applyReverseInOrder(root.right, sum)

    # Store value of the root node.
    rootVal = root.val

    # Replace the value at root node with the sum of all the nodes which have value greater than the root.val.
    root.val = sum

    # Store the sum.
    sum = sum + rootVal

    # Go to the left sub tree.
    sum = applyReverseInOrder(root.left, sum)
    return sum


def convertBstToGreaterSum(root):
    sum = 0

    # Apply reverse inorder.
    applyReverseInOrder(root, sum)
    return root


# Fast input.
def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = TreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = TreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = TreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root


def printLevelOrder(root):
    q = Queue()
    if(root == None):
        return

    q.put(root)

    while(q.qsize() > 0):
        currentNode = q.get()

        print(currentNode.val, end=" ")

        if(currentNode.left != None):
            q.put(currentNode.left)

        if(currentNode.right != None):
            q.put(currentNode.right)

    print()


# Main.
t = int(input().strip())
for i in range(t):
    root = takeInput()
    bstToGreaterSum = convertBstToGreaterSum(root)
    printLevelOrder(bstToGreaterSum)
