def sum_n(x):
    if x == 0:
        return 0
    return x + sum_n(x-1)
n = int(input())
print(sum_n(n))