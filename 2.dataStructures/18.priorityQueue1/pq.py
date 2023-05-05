class PriorityQueueNodes:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority



class PriorityQueue :

    def __init__(self):
        self.pq = []
    
    def getSize(self):
        return len(self.pq)
    def isEmpty(self):
        return self.getSize() == 0
 
    def getMin(self):
        if self.isEmpty is True:
            return None
        return self.pq[0].value
    def __percolateUp(self):
        childIndex = self.getSize()-1
        while childIndex > 0:
            parentIndex = (childIndex - 1)// 2
            if self.pq[childIndex].priority < self.pq[parentIndex].priority:
                self.pq[childIndex],self.pq[parentIndex]= self.pq[parentIndex],self.pq[childIndex]
                childIndex = parentIndex
            else:
                break
    
    def __precolateDown(self):
        parentIndex = 0
        leftIndex = 2*parentIndex + 1
        rightIndex = 2*parentIndex + 2
        while leftIndex < self.getSize():
            minIndex = parentIndex
            if(self.pq[minIndex].priority > self.pq[leftIndex].priority):
                minIndex = leftIndex
            if(rightIndex < self.getSize() and self.pq[minIndex].priority > self.pq[rightIndex].priority):
                minIndex = rightIndex
            
            if minIndex!=parentIndex:
                self.pq[parentIndex],self.pq[minIndex] = self.pq[minIndex],self.pq[parentIndex]
                parentIndex = minIndex
                leftIndex = 2*parentIndex + 1
                rightIndex = 2*parentIndex + 2
            else:
                break


    def insert(self,value,priority):
        pqNode = PriorityQueueNodes(value,priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    
    def removeMin(self):
        if self.isEmpty():
            return None
        element = self.pq[0]
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return element.ele

