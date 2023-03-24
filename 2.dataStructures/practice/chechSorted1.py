def sorted(arr,si):
    l = len(arr)
    if si == l-1 or si == l:
        return True
    if arr[si] > arr[si+1]:
        return False
    return sorted(arr,si+1)


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sorted(arr,0))