#code is contributed by Lokesh Poluru Velayudham

n = int(input())
for i in range(65,66+n):
    for j in range(65,i+1):
        print(chr(i),end="")
    print()
