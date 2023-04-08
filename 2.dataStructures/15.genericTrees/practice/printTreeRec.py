class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()

def printTree(root):
    # its a edge case
    if root is None:
        return
    print(root.data)
    for child in root.children:
        printTree(child)

def printDetailedTree(root):
    if root is None:
        return
    print(root.data,":", end="")

    for child in root.children:
        print(child.data,",",end="")

    print()

    for child in root.children:
        printDetailedTree(child)


def takeTreeInput():
    print("enter root data")
    rootData = int(input())
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    print("enter the no of children for ", rootData)
    childrenCount = int(input())

    for i in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    return root


# n1 = TreeNode(5)
# n2 = TreeNode(2)
# n3 = TreeNode(9)
# n4 = TreeNode(8)
# n5 = TreeNode(7)
# n6 = TreeNode(15)
# n7 = TreeNode(1)


# n1.children.append(n2)
# n1.children.append(n3)
# n1.children.append(n4)
# n1.children.append(n5)

# n3.children.append(n6)
# n3.children.append(n7)
root = takeTreeInput()
printDetailedTree(root)