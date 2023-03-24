from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)

class node():
    def __init__(self,data):
        self.data = data
        self.next = None


# Take input 
def takeInput():
    head = None
    tail = None
    
    datas = list(map(int,stdin.readline().strip().split(" ")))

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
        print(str(head.data),end=" ")
        head = head.next
    print()

def merge(head1,head2):

    if head1 is None:
        return head2
    
    if head2 is None:
        return head1
    
    fh,ft = None, None
    
    if head1.data < head2.data:
        fh = head1
        ft = head1
        head1 = head1.next
    else:
        fh = head2
        ft = head2
        head2 = head2.next

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            ft.next = head1
            ft = ft.next
            head1 = head1.next
        else:
            ft.next = head2
            ft = ft.next
            head2 = head2.next
    if head1 is not None:
        ft.next = head1
    if head2 is not None:
        ft.next = head2
    
    return fh



    # fH = node(1)
    # fT = fH
    # while head1 is not None and head2 is not None:
    #     if(head1.data < head2.data):
    #         fT.next = head1
    #         fT = fT.next
    #         head1 = head1.next
    #     else:
    #         fT.next = head2
    #         fT = fT.next
    #         head2 = head2.next
    # while head1 is not None:
    #     fT.next = head1
    #     fT = fT.next
    #     head1 = head1.next
    
    # while head2 is not None:
    #     fT.next = head2
    #     fT = fT.next
    #     head2 = head2.next
    # return fH.next


# main
t = int(stdin.readline().strip())

while t > 0:
    head1 = takeInput()
    head2 = takeInput()
    # printLL(head1)
    # printLL(head2)
    newHead = merge(head1,head2)
    printLL(newHead)
    t -= 1