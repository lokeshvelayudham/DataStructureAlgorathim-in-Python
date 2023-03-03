#code is contributed by Lokesh Poluru Velayudham

n = int(input())


for i in range(n+1):
    c = chr(ord('A') + i -1)
    for j in range(1,i+1):
        p = chr(ord(c)+j-1)
        print(p,end="")
    print()