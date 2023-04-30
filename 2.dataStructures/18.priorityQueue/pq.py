class PriorityQueueNodes:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority



class PriorityQueue :

    def __init__(self):
        self.pq = []
    
    def getMin(self):
        