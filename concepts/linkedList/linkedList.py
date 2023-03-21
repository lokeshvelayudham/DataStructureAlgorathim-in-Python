class node:

    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    
    while head is not None:
        print(str(head.data)+"->",end="")
        head = head.next
    print("None")
    return 



def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            # Approach O(n)
            tail.next = newNode
            tail = newNode
            # approcaj O(n2)
            # curr = head    
            # while curr.next is not None:
            #     curr = curr.next
            # curr.next = newNode
    return head
        


head = takeInput()
printLL(head)
