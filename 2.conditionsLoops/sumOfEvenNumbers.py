
#code is contributed by Lokesh Poluru Velayudham

n = int(input())
even = 0
for i in range(n+1):
    if(i%2 == 0):
        even += i
print(even)