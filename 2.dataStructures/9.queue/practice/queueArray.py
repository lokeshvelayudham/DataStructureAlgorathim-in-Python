class queue :
    def __init__(self) :
        self.__data = []
        self.__front = 0
        self.__count = 0
    
    def enqueue(self,item) :
        self.__data.append(item)
        self.__count += 1

    
    def dequeue(self) :
        if self.__count == 0 :
            return -1
        ele = self.__data[self.__front]
        self.__front += 1
        self.__count -= 1
        return ele
    
    
    def front(self) :
        if self.__count == 0 :
            return -1
        return self.__data[self.__front]
    
    def size(self) :
        return self.__count
    
    def isEmpty(self) :
        return self.size() == 0
    

q = queue()
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
q.enqueue(13)

while(q.isEmpty() is False) :
    print(q.front())
    q.dequeue()

print(q.dequeue())