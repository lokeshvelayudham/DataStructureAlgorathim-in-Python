from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def skipMdeleteN(head, M, N) :
    if head is None or  M == 0 :
        return None
    if N == 0 :
        return head
    
    curr = head 
    temp = None

    while curr is not None :
        take = 0
        skip = 0
        # take loop 
        while curr is not None and take < M :
            if temp is None :
                temp = curr
            else :
                temp.next = curr
                temp = curr
            curr = curr.next
            take += 1
        # skip loop 
        while curr is not None and skip < N :
            curr = curr.next
            skip += 1

    if temp is not None :
        temp.next = None

    return head


#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1