
from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

# linked list
def LL(head):
    ls = []
    while head is not None:
        ls.append(head.data)
        head = head.next
    return ls
    
# reversed linked list
def revLL(head):
    rl = []
    while head is not None:
        rl.insert(0,head.data)
        head = head.next
    return rl

def isPalindrome(head) :
    if LL(head) == revLL(head):
        return True
    else:
        return False


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


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    # printLinkedList(head)
    
    if isPalindrome(head) :
        print('true')
    else :
        print('false')
        
    t -= 1