# MergeSort Linked list
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
# class to create a node
class node() :
    def __init__(self, data) :
        self.data = data
        self.next = None

# find the mid of the linked list 
def findMid(head) :
    if head is None :
        return None
    slow = fast = head
    while fast.next is not None and fast.next.next is not None :
        slow = slow.next
        fast = fast.next.next
    return slow

# merge sorted linked list
def merge(a1,a2) :
    if a1 is None :
        return a2
    if a2 is None :
        return a1
    
    finalHead, finalTail = None, None

    if a1.data < a2.data :
        finalHead = a1
        finalTail = a1
        a1 = a1.next
    else :
        finalHead = a2
        finalTail = a2
        a2 = a2.next
    
    while a1 is not None and a2 is not None :
        if a1.data < a2.data :
            finalTail.next  = a1
            finalTail = finalTail.next
            a1 = a1.next
        else :
            finalTail.next = a2
            finalTail = finalTail.next
            a2 = a2.next

    if a1 is not None :
        finalTail.next = a1
    if a2 is not None :
        finalTail.next = a2

    return finalHead


# divide the linked list into two
def mergeSort(head):
    if head is None or head.next is None :
        return head
    mid = findMid(head)
    a1 = head
    a2 = mid.next
    mid.next = None

    a1 = mergeSort(a1)
    a2 = mergeSort(a2)

    a = merge(a1,a2)

    return a

# Take input of linked list
def takeInput() :
    head = None
    tail = None
    datas = list(map(int,stdin.readline().rstrip().split()))

    for currData in datas :
        if currData == -1 :
            break
        newNode = node(currData)
        if head is None :
            head = newNode
            tail = newNode
        else :
            tail.next = newNode
            tail = newNode
    return head

# print Linkde list
def printLL(head) :
    while head is not None :
        print(str(head.data), end= " ")
        head = head.next
    print()
    


# main
t = int(stdin.readline().strip())

while t > 0:
    head = takeInput()
    # printLL(head)
    # a = findMid(head)
    # print(a.data)
    sort = mergeSort(head)
    printLL(sort)

    t -= 1