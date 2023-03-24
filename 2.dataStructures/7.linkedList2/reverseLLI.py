from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)

# Class to create node
class node():
    def __init__(self,data):
        self.data = data
        self.next = None
# take input
def takeInput():
    head = None
    tail = None
    datas = list(map(int,stdin.readline().rstrip().split()))
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
        print(str(head.data),end= " ")
        head = head.next
    print()
# Reverse Linked list itterative 
def reverseLL(head):
    curr = head 
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev 
        prev = curr
        curr = next
    head = prev
    return head
# Main
t = int(stdin.readline().strip())
while t > 0:
    head = takeInput()
    # printLL(head)
    rl = reverseLL(head)
    printLL(rl)
    t -= 1