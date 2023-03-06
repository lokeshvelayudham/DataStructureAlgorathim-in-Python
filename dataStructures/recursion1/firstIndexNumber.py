def firstIndex(arr, x, si):
    l = len(arr)
    if si == l-1 or si == l:
        return -1
    if arr[si] == x:
        return si
    return firstIndex (arr, x, si+1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x, 0))
