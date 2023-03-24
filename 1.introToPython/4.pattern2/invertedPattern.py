n = int(input())
p = n
for i in range(n):
    for j in  range(n-i):
        print(p, end="")
    p-=1
    print()