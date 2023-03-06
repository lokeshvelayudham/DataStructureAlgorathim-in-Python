def sumArray(arr,n):
    if n <= 0: 
        return 0
    else:
        return arr[n-1] + sumArray(arr,n-1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
n = len(arr)
print(sumArray(arr,n))
