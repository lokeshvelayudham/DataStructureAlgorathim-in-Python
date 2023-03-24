import sys
sys.setrecursionlimit(5000)
sys.set_int_max_str_digits(50000)
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
n = int(input())
print(fact(n))
