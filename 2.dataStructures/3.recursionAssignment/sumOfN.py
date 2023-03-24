#code is contributed by Lokesh Poluru Velayudham


# Approach 1

def sum(n):
    if n <= 0:
        return 0
    else:
        return n%10 + sum(n//10)
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
print(sum(n))


# Approach 2

"""
def sumArray(arr,n):
    if n <= 0: 
        return 0
    else:
        return arr[n-1] + sumArray(arr,n-1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

n = input()
arr = [int(i) for i in n]
n = len(arr)
print(sumArray(arr,n))

"""