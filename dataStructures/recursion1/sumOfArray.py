def sumArray(arr):
    sum = 0
    # Please add your code here
    for i in range(len(arr)):
        sum+=arr[i]
    return sum

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
