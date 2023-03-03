#code is contributed by Lokesh Poluru Velayudham

n = int(input())

for i in range(n+1):
    #space
    for s in range(n-i):
        print(" ",end="")
    #star increase
    for st in range(i):
        print("*",end="")
    # star mirror
    for st in range(i-1):
        print("*",end="")
    print()