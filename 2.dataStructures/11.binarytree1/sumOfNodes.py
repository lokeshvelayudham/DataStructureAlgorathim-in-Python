#code is contributed by Lokesh Poluru Velayudham


from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10 ** 6)
# create a class for binary nodes
class binaryNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
    
# sum of the nodes
def getSum(root):
    if root is None:
        return 0
    return root.data + getSum(root.left) + getSum(root.right)

#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    root = binaryNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = binaryNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = binaryNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

# Main
root = takeInput()
print(getSum(root))