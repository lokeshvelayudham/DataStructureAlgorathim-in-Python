def lastIndex(arr, x, si):
    # l = len(arr)
    if si == -1:
        return -1
    elif arr[si] == x:
        return si
    return lastIndex (arr, x, si-1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
si = len(arr) - 1
print(lastIndex(arr, x, si))
