from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
# node class

class node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
# Take input 
def takeInput():
    head = None
    tail = None
    datas = list(map(int,stdin.readline().rstrip().split(" ")))

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


#  print Linked List LL
def printLL(head):
    while head is not None:
        print(str(head.data),end=" ")
        head = head.next
    print()
    

# Reverse Linked list
def reverseLL(head):
    if head is None or head.next is None:
        return head,head
    smallHead,smallTail = reverseLL(head.next)
    smallTail.next = head
    head.next = None
    return smallHead,head
# main Function
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    printLL(head)
    sH,sT =reverseLL(head)
    printLL(sH)
    t -= 1