#code is contributed by Lokesh Poluru Velayudham



n=int(input())
l=list(map(int,input().split()))
ma=l[-1]
l=l[::-1]
k=[l[0]]
for i in range(1,n):
    if l[i]>=ma:
        ma=l[i]
        k.append(l[i])
k=k[::-1]
print(*k)