
from sys import stdin


def pairsum(arr, n, x):
    # count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]+arr[j] == x:
                print (arr[i],arr[j])
    # return

    #Your code goes here

n,x = input().split(" ")
n = int(n)
x = int(x)
# print(x)
arr = list(map(int, stdin.readline().strip().split(" ")))
# print(arr)
# print(len(arr))
print(pairsum(arr,n,x))