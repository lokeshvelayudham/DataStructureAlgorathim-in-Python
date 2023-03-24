from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)


# Class created for node Creation

class node():
    def __init__(self,data):
        self.data = data
        self.next = None


# input Function 

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

# print Linked List
def printLL(head):
    while head is not None:
        print(str(head.data),end = " ")
        head = head.next
    print()

# reverse Linked list O(n^2)
def reverseLL1(head):
    if head is None or head.next is None:
        return head
    smallHead = reverseLL1(head.next)
    curr = smallHead
    while curr.next is not None:
        curr = curr.next
    curr.next = head
    head.next = None
    return smallHead

# Reverse Linked list O(N)
def reverseLL2(head):
    if head is None or head.next is None:
        return head,head
    smallHead,smallTail = reverseLL2(head.next)
    smallTail.next = head
    head.next = None
    return smallHead,head

# Reverse linked lsit O(n) optimized code
def reverseLL3(head):
    if head is None or head.next is None:
        return head
    smallHead = reverseLL3(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallHead
# Main Function
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    printLL(head)
    # r1 = reverseLL1(head)
    # printLL(r1)
    # r2,r3 = reverseLL2(head)
    # printLL(r2)
    r3 = reverseLL3(head)
    printLL(r3)



    t -= 1
