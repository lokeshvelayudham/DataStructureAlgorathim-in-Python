def max_valleys(t, test_cases):
    results = []
    
    for _ in range(t):
        n, m, heights = test_cases[_]
        
        dp = [1] * n
        
        for i in range(n):
            for j in range(i - m, i):
                if j >= 0 and heights[j] < heights[i]:
                    dp[i] = max(dp[i], dp[j])
        
        max_valleys = max(dp)
        results.append(max_valleys)
    
    return results

# Read the input
t = int(input())
test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))
    test_cases.append((n, m, heights))

# Calculate the maximum number of valleys Ninja can visit for each test case
results = max_valleys(t, test_cases)

# Print the results
for res in results:
    print(res)
