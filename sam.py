#code is contributed by Lokesh Poluru Velayudham


from sys import stdin
import math

def arrayEquilibriumIndex(arr, n) :
    # O(n) time approach
    totalSum = sum(arr)
    leftSum = 0
    for i in range(n):
        rightSum = totalSum - leftSum - arr[i]
        if (rightSum == leftSum):
            return i
        leftSum += arr[i]
    return -1
 


# approcah 2 O(n^2)

    # for i in range(n):
    #     leftSum = 0
    #     rightSum = 0

    #     # leftSum
    #     for j in range(i):
    #         leftSum += arr[j]
        
    #     # rightSum
    #     for j in range(i+1,n):
    #         rightSum += arr[j]
        
    #     # check equilibrium
    #     if leftSum == rightSum:
    #         return i
    
    # return -1
  
    





#Taking input using fast I/O method
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
    print(arrayEquilibriumIndex(arr, n))

    t-= 1