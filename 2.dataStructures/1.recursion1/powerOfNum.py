## Write your code here
## To take space separated input for two variables, we use the following syntax (3 lines)
def power(n,p):
    if p == 0:
        return 1
    return n * power(n,p-1)

n, p = input().split()
n = int(n)
p = int(p)
print(power(n,p))
