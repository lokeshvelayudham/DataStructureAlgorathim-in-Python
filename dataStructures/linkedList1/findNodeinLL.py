from sys import stdin
class node():
    def __init__(self,data):
        self.data = data
        self.next = None


# take input
def takeInput():
    datas = list(map(int,stdin.readline().rstrip().split(" ")))

    head = None
    tail = None

    for currData in datas:
        if currData == -1:
            break
        newNode = node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head



# print linked list 
def printLL(head):

    while head is not None:
        print(str(head.data)+"->",end=" ")
        head = head.next
    print(None)
# find node
def findNode(head,d):
    curr = head
    count = 0 
    while curr is not None:
        if curr.data == d:
            return count
        count += 1
        curr = curr.next
    return -1

# main

t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    d =int(stdin.readline().rstrip())
    l= findNode(head,d)
    print(l)
    # printLL(head)
    
    t -= 1