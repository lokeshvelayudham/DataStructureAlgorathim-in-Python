
import math
def minSideJumps(obstacles):
    n = len(obstacles) - 1
    dp = [math.inf] * 3
    prev = [1, 0, 1]

    for i in range(1, n + 1):
        # same lane
        dp[0] = math.inf if obstacles[i] == 1 else prev[0]
        dp[1] = math.inf if obstacles[i] == 2 else prev[1]
        dp[2] = math.inf if obstacles[i] == 3 else prev[2]

        # 1st pass: top to bottom
        if obstacles[i] != 2:
            dp[1] = min(dp[1], dp[0] + 1)
        if obstacles[i] != 3:
            dp[2] = min(dp[2], dp[1] + 1, dp[0] + 1)

        # 2nd pass: bottom to top
        if obstacles[i] != 2:
            dp[1] = min(dp[1], dp[2] + 1)
        if obstacles[i] != 1:
            dp[0] = min(dp[0], dp[1] + 1, dp[2] + 1)
        
        prev = dp
    
    return min(prev)
# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the input for the current test case
    n = int(input())
    manholes = list(map(int, input().split()))

    # Find the minimum number of lane changes
    min_changes = minSideJumps(manholes)

    # Print the result for the current test case
    print(min_changes)
