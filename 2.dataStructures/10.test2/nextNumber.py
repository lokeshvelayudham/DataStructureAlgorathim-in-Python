## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None




def reverseLL(head):
    prev = None
    current = head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def nextNumber(head):
    head = reverseLL(head)
    carry = 1
    temp = head
    while(temp is not None):
        sum = temp.data + carry
        temp.data = sum%10
        carry = sum//10
        temp = temp.next
    
    if carry==1:
        temp = head
        while(temp.next is not None):
            temp = temp.next
        newNode = Node(carry)
        temp.next = newNode
    
    return reverseLL(head)
   
        
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head is not None:
        print(head.data,end= ' ')
        head = head.next
    return

# Main
# Read the link list elements including -1
arr=[int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = nextNumber(l)
printll(head)