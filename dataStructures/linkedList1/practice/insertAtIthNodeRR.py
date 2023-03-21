from sys import stdin

#code is contributed by Lokesh Poluru Velayudham

#Following is the Node class already written for the Linked List
class node :
    def __init__(self, data) :
        self.data = data
        self.next = None

# length of linked list 
def length(head):
    count = 0
    while head is not None:
        count +=1
        head = head.next
    return count



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

    



#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print(None)


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    i = int(stdin.readline().rstrip())
    d = int(stdin.readline().rstrip())
    l = insertAtIthPositionR(head, i, d)    
    printLinkedList(l)


    t -= 1