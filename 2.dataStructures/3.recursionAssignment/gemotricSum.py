#code is contributed by Lokesh Poluru Velayudham


def geometric(n):
    if n < 0:
        return 0
    elif n  ==  0:
        return 1
    else:
        return  1/(2**n) + geometric(n-1)
    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
a = geometric(n)
print("%.5f" % a)

