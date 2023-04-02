from sys import stdin, setrecursionlimit
setrecursionlimit (10 ** 6)

class node :
    def __init__(self,data) :
        self.data = data
        self.next = None

class queue :
    def __init__(self) :
        self.__head = None
        self.__tail = None
        self.__count = 0
        # self.__front = 0
    
    def enqueue(self,item) :
        self.__count += 1
        newNode = node(item)
        if self.__head == None:
            self.__head = newNode
            self.__tail = newNode
        else :
            self.__tail.next = newNode
            self.__tail = newNode
        
    
    def dequeue(self) :
        if self.isEmpty():
            return -1
        ans = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return ans

    def front(self) :
        if self.isEmpty():
            return -1 
        return self.__head.data
    
    def size(self) :
        return self.__count 
    
    def isEmpty(self):
        return self.size() == 0



#main
p = int(stdin.readline().strip())

q = queue()

while p > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        q.enqueue(data)

    elif choice == 2 :
        print(q.dequeue())

    elif choice == 3 :
        print(q.front())

    elif choice == 4 : 
        print(q.size())

    else :
        if q.isEmpty() :
            print("true")
        else :
            print("false")

    p -= 1