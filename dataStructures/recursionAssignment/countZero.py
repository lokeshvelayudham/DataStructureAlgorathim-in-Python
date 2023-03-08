#code is contributed by Lokesh Poluru Velayudham

c = 0
def countZero(n):
    global c 
    if n == 0:
        return 1
    if n > 0:
        if n % 10 == 0:
            c+=1 
        countZero(n // 10)
    return c






# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
print(countZero(n))


