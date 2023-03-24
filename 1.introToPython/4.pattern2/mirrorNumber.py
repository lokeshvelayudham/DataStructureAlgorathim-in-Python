#code is contributed by Lokesh Poluru Velayudham

n = int(input())
for i in range(1,n+1):
    #space
    for space in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()

