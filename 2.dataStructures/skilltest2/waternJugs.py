cases = int(input())

for k in range(cases):
    a, b, c = map(int, input().split())
    s1 = []
    s2 = []
    
    if a < b:
        a, b = b, a
    
    for i in range(b):
        s1.append(1)
        s2.append(1)
    
    for i in range(a - b):
        s1.append(s2[0])
        s2.pop()
    
    for i in range(a):
        s1.pop()
    
    while len(s2) != 0:
        s1.append(s2[0])
        s2.pop()
    
    total_sum = sum(s1)
    
    if (total_sum + b) == c or (total_sum + b - a) == c:
        print("Yes")
    else:
        print("No")
