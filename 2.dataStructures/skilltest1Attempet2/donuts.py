t = int(input())

for _ in range(t):
    n = int(input())
    
    weights = list(map(int, input().split()))
    weights.sort(reverse=True)
    
    max_weight = 0
    cnt = 0
    for i in range(2, n, 3):
        if cnt < n // 4:
            max_weight += weights[i]
            cnt += 1
        else:
            break
    
    print(max_weight)
