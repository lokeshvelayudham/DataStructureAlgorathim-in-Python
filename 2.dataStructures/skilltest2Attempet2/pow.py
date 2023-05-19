from functools import reduce


def superPow(a,b):
    # Compute a_mod = a mod 1337
    a_mod = a % 1337
    
    # Compute n, the number represented by the array b, using reduce()
    n = reduce(lambda x, y: (x * 10 + y) % 1140, b, 0)
    
    # Compute a_mod raised to the power of n using repeated squaring
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * a_mod) % 1337
        a_mod = (a_mod * a_mod) % 1337
        n //= 2
    
    # Return the result modulo 1337
    return result % 1337
a = int(input())
n = int(input())
b = list(map(int, input().split()))
ans = superPow(a,b)
print(ans)