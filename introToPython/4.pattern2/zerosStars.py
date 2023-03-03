#code is contributed by Lokesh Poluru Velayudham

n = int(input())

for i in range(n):
    for j in range(n):
        if j == i:
            print("*",end="")
        else:
            print(0,end="")
    print("*",end="")
    for j in range(n,0,-1):
        if j == i+1:
            print("*",end="")
        else:
            print(0,end="")
    print()
