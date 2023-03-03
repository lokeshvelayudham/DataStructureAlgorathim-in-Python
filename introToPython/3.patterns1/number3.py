#code is contributed by Lokesh Poluru Velayudham

n = int(input())
print(1)
for i in range(1,n):
    for j in range(i+1):
        if (j == 0 or j == i):
            print(1,end ="")
        else:
            print(2,end="")
    print()
