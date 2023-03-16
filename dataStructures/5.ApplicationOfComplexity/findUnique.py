from sys import stdin
from collections import defaultdict

def findUnique(arr, n) :
    dic={}                 
    for i in arr: 
        # print(dic)         
        dic[i]=0
        # print(dic)
                  
    for i in arr:
        dic[i] +=1
        print(dic)
    
    for i in arr:
        # print(dic)         
        if dic[i] ==1:    
           return i
 




#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(findUnique(arr, n))

    t-= 1