from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
class node :
    def __init__(self, data) :
        self.data = data
        self.next = None

class stack :
    def __init__(self) :
        self.__head = None
        self.__count = 0

    def push(self, item) :
        newNode = node(item)
        newNode.next = self.__head
        self.__head = newNode
        self.__count += 1
    
    def pop(self) :
        if self.isEmpty() is True :
            return -1
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1

        return data
    
    def top(self):
        if self.isEmpty() is True:
            # print("Hey! Stack is Empty!!")
            return -1
        
        return self.__head.data
    
    def size(self):
        return self.__count
        
    def isEmpty(self):
        return self.size() == 0 
    

q = int(stdin.readline().strip())

stack = stack()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2 :
        print(stack.pop())

    elif choice == 3 :
        print(stack.top())

    elif choice == 4 : 
        print(stack.size())

    else :
        if stack.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1