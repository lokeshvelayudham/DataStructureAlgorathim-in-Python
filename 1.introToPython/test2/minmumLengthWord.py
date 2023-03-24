#code is contributed by Lokesh Poluru Velayudham


s  = input().split()
m = []
for i in s:
    m.append(len(i))
print(s[m.index(min(m))])