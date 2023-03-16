from sys import stdin
import sys


def pairSum(arr, n, num) :
    un = {}
    count = 0
    
    for i in range(n):
        if num - arr[i] in un:
            count += un[num - arr[i]]
        if arr[i] in un:
            un[arr[i]] += 1
        else:
            un[arr[i]] = 1
    return count

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
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))

    t -= 1