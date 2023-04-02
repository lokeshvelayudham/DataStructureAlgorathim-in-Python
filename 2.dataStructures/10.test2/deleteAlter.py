''' 
    Following is the node structure

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

'''
class node :
    def __init__(self,data):
        self.data = data
        self.next = next


def deleteAlternateNodes(head):
    if head == None :
        return
    curr = head
    new = head
    while (curr != None and curr.next != None):
        new = curr.next
        curr.next = new.next

        curr = curr.next

     
    
    
