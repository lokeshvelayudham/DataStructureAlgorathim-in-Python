class mapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucketSize = 10
        self.bucket = [None for i in range(self.bucketSize)]
        self.count = 0
    
    def size(self):
        return self.count
    
    def getBucketIndex(self,hc):
        return (abs(hc) % (self.bucketSize))
    
    def getValue(self,key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
    
    def remove(self,key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.bucket[index] = head.next

                else:
                    prev.next = head.next
                self.count -= 1
                return head.value
            

            prev = head
            head = head.next
        return None
    
    def rehash(self):
        temp = self.bucket
        self.bucket = [None for i in range(2*self.bucketSize)]
        self.bucketSize = 2 * self.bucketSize
        self.count = 0
        for head in temp:
            while head is not None:
                self.inset(head.key,head.value)
                head = head.next
                

    def insert(self,key,value):

        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        head = self.bucket[index]

        newNode = mapNode(key,value)
        newNode.next = head
        self.bucket[index] = newNode
        self.count += 1
        loadFactor = self.count/self.bucketSize
        if loadFactor >= 0.7:
            self.rehash()
