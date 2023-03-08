#code is contributed by Lokesh Poluru Velayudham


def staircase(n):
    if (n == 0):
        return 1
    elif n < 0:
        return 0
    else:
        return staircase(n-1) + staircase(n-2) + staircase(n-3)
    
    pass

n = int(input())
print(staircase(n))