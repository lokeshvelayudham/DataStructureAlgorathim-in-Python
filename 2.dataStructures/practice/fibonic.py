import time
def fib(n):
    if n == 1 or n ==2:
        return 1
    return fib(n-1) + fib(n-2)



n = int(input())
st = time.time()
ans = fib(n)
et = time.time()
print(ans)
print(st)
print(et)