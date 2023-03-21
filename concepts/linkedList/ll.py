from sys import stdin
# #code is contributed by Lokesh Poluru Velayudham

# creating a linked list using class function
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
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

# print Linked List

def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end=" ")
        head = head.next
    print(None)

# print ith element in the linked list
def printIth(head,i):
    curr = head
    count = 0
    while curr is not None:
        if count == i:
            print(curr.data)
        count +=1
        curr = curr.next

# length of linked list approach 1:
def lengthLL1(head):
    count = 0
    while head is not None:
        count +=1
        head = head.next
    return count

# length of a linked list appraoch 2:
def lengthLL2(head):
    if head is None:
        return 0
    return 1+ lengthLL2(head.next)

# insert at Ith element 
def insertIth(head,i,d):
    if i < 0 or i>lengthLL1(head):
        return head
    
    curr = head
    prev = None
    count = 0
    while count < i:
        prev = curr
        curr = curr.next
        count+=1
    newNode = node(d)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr
    return head

# insert at I th position recrusivley 
def insertAtIthPositionR(head, i, d):

    if i < 0:
        return head
    if i == 0:
        newNode = node(d)
        newNode.next = head
        return newNode
    if head is None:
        return None
    smallHead = insertAtIthPositionR(head.next,i-1,d)
    head.next = smallHead

    return head

    
# Delete node at I th position 
def deleteNode(head,i):
    if head is None:
        return head
    if i == 0:
        return head.next
    
    curr = head
    count = 0
    while curr is not None and count <(i-1):
        count+=1
        curr = curr.next
    if curr is None or curr.next is None:
        return head
    curr.next = curr.next.next

    return head
# Main function 
print("total test cases")
t = int(stdin.readline().rstrip())

while t > 0 :
    print("enter inputs")
    head = takeInput()
    printLL(head)
    print("enter I th value to print and modify")
    i = int(stdin.readline().rstrip())
    print("the I th element in the lined list is ")
    printIth(head,i)
    print("length of the linked list is :")
    l1 = lengthLL1(head)
    print(l1)
    print("length of the linked list is :")
    l2 = lengthLL2(head)
    print(l2)
    print("enter the data to be added in the i th Position")
    d = int(stdin.readline().rstrip())
    ins = insertIth(head,i,d)
    printLL(ins)
    de = deleteNode(head,i)
    print("the i th postion of element will be deleted")
    printLL(de)
    t-=1