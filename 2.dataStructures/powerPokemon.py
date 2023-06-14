MOD = int(1e9) + 7

def count_bit_strings(n, k):
    # Initialize the dp array
    dp = [[0] * (k+2) for _ in range(n+1)]
    dp[1][0] = 1
    dp[1][1] = 1

    # Compute the dp array
    for i in range(2, n+1):
        for j in range(k+1):
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j+1]) 

    return dp[n][k] 

# Read the input
T = int(input())

# Process each test case
for _ in range(T):
    n, k = map(int, input().split())
    result = count_bit_strings(n, k)
    print(result)
