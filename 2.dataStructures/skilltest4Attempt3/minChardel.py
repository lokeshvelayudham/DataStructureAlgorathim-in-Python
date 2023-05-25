'''
    Time Complexity = O(N * logM)
    Space Complexity = O(M)
    
    Where 'N' is the length of the string.
    Where 'M' is the number of unique characters in the string.
'''

import heapq
from sys import stdin

def minCharDeletion(str):
    length = len(str)

    # Counter of characters to delete.
    count = 0
    
    mapp = {}
    
    # Storing frqquency of each character in the dictionary.
    for i in str:
        mapp[i] = mapp.get(i,0)+1
        
    pq = []
    
    # Put frequencies of characters into the list.
    for key in mapp.keys():
        currFreq = mapp[key]
        pq.append(currFreq)
        pq.sort(reverse = True)
        
    while len(pq)>0:
        # Take the biggest frequency character.
        mostFrequent = pq[0]
        pq.pop(0)
        
        # If priority queue is empty, then return the number of characters to be deleted.
        if len(pq) == 0:
            return count
        
        # If this frequency is equal to the next one, decrease it by 1 and put back to the priority queue.
        if mostFrequent == pq[0]:  
            if mostFrequent>1:
                pq.append(mostFrequent-1)
                pq.sort(reverse = True)    
            count +=1
    # Return the number of characters to be deleted.      
    return count

#Main        
t = int(input())
while t > 0:
    s = stdin.readline().strip()
    print(minCharDeletion(s))
    t -= 1