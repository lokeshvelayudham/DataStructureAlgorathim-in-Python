def power(x, n):
    # base case
    if n == 0:
        return 1
    if n < 0:
        return(1/ power(x,-n))
    if(n % 2 == 0):
                return power(x,n/2)*power(x,n/2)
    else:
          return x*power(x,(n-1)/2)*power(x,(n-1)/2)


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
