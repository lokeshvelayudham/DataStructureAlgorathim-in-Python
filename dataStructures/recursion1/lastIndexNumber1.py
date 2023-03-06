def lastIndex(arr, x):
    l = len(arr)
    if l == 0:
        return -1
    nArr = arr[1:]
    if lastIndex(nArr,x) != -1:
        return lastIndex(nArr,x) + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
si = len(arr) - 1
print(lastIndex(arr, x))
