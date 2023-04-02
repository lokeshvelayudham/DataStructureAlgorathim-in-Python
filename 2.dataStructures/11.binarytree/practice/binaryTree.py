# node class to create a binary tree

class binaryNode :
    def __init__(self,data) :
        self.data = data 
        self.left = None
        self.right = None


# print the binary tree
def printTree(root) :
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

# take input for the binary tree 
def treeInput() :
    rootData = int(input())
    if rootData == -1:
        return None
    
    root = binaryNode(rootData)
    root.left = treeInput()
    root.right = treeInput()


    return root


# count number of nodes
def numNodes(root) :
    if root is None:
        return 0 
    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)

    return 1 + leftCount + rightCount

# btn1 = binaryNode(1)
# btn2 = binaryNode(2)
# btn3 = binaryNode(3)
# btn4 = binaryNode(4)
# btn5 = binaryNode(5)

# btn1.left = btn2
# btn1.right = btn3
# btn2.left = btn4
# btn2.right = btn5

root = treeInput()
printTree(root)
print("number of nodes in the tree:",numNodes(root))