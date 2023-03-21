from sys import stdin
# #code is contributed by Lokesh Poluru Velayudham
# node creation class
class node():
    def __init__(self,data):
        self.data = data
        self.next = None


# take input function 
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


# print Linked list
def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end=" ")
        head = head.next
    print(None)


# length of the Linked list 
def lengthLL(head):
    count = 0
    while head is not None:
        count+=1
        head = head.next
    return count

# length of the linked list recurcive
def lengthLLR(head):
    if head is None:
        return 0
    return 1 + lengthLLR(head.next)


# print I th element in the linked list
def printIth(head,i):
    count = 0
    while head is not None:
        if count == i:
            print(head.data)
        head = head.next
        count +=1

# Main function
t = int(stdin.readline().rstrip())
while t > 0:
    print("enter the datas")
    head = takeInput()
    print("the linked list is ")
    printLL(head)
    print("the length of the linked list is: ")
    l = lengthLL(head)
    print(l)
    print("the length of the linked list by recrusion:")
    lr = lengthLLR(head)
    print(lr)
    print("enter the I th element to view or modify")
    i = int(stdin.readline().rstrip())
    print("the i th element in the linked list")
    printIth(head,i)

    t-=1