from sys import stdin
import math

def arrayEquilibriumIndex(arr, n) :
    totalSum = sum(arr)
    leftSum = 0
    index = 0
    while index < n:
        rightSum = totalSum - leftSum - arr[index]
        if (rightSum == leftSum):
            return index
        leftSum = leftSum + arr[index]
        index +=1
    
    return -1
    

    #Your code goes here



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