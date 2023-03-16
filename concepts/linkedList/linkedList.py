class node:

    def __init__(self, data):
        self.data = data
        self.next = None

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = node(currData)
        if head is None:
            head = newNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
        



a = node(13)
b = node(15)
a.next = b
print(a.data)
print(b.data)
print(a.next.data)
print(a.next.next)
print(a)
print(b)
print(a.next)
