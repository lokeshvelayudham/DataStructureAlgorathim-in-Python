from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
# #code is contributed by Lokesh Poluru Velayudham



#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def findNodeRec(head, n) :
	#Your code goes here
    if head is None:
        return -1
    if head.data == n :
        return 0
    new = findNodeRec(head.next, n)
    if new == -1 :
        return -1
    else :
        return 1 + new


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
    n = int(stdin.readline().rstrip())    

    print(findNodeRec(head, n))

    t -= 1