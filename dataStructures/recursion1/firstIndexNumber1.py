def firstIndex(arr,x):
    l = len(arr)
    if l == 0:
        return -1
    if arr[0] == x:
        return 0
    nArr = arr[1:]
    if firstIndex(nArr,x) == -1:
        return -1
    else:
        return firstIndex(nArr,x) + 1



# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))