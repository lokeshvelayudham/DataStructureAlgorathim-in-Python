from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)

class node():
    def __init__(self,data):
        self.data = data
        self.next = None


# take input
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
            tail =newNode
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

# midpoint find
def midPoint(head):
    if head is None:
        return head
    slow = head 
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow

# main Function 
t = int(stdin.readline().strip())

while t > 0:
    head = takeInput()
    # printLL(head)
    r1 = midPoint(head)
    if r1 is not None:
        print(r1.data)

    t -= 1
