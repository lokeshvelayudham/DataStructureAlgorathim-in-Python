def mul(m,n):
    if m <= 0 or n <= 0:
        return 0
    else:
        return m + mul(m,n-1)


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
m = int(input())
n = int(input())
print(mul(m,n))