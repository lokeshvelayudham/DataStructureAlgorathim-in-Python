def checkNumber(arr, x):
    l = len(arr)
    if l == 0:
        return False
    elif arr[0] == x:
        return True
    nArr = arr[1:]
    return checkNumber(nArr,x)
   

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
# l = len(arr)
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
