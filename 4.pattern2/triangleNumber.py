#code is contributed by Lokesh Poluru Velayudham

n = int(input())

for i in range(1,n+1):
    #space
    for s in range(n-i):
        print(" ",end="")
    #increase
    p = i
    for st in range(i):
        print(p,end="")
        p += 1
    #decrease 
    q = p -2
    for st in range(i-1):
        print(q,end="")
        q -= 1
    print()