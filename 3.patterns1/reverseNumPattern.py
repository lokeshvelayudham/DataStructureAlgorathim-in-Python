#code is contributed by Lokesh Poluru Velayudham

n = int(input())
p = n
for i in range(n+1):
    p = i
    for j in range(i):
        print(p,end="")
        p-=1
    print()