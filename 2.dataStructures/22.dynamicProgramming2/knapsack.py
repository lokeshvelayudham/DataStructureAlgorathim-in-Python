# def knapsack(W,val,wt,n,i):
#     if i == n:
#         return 0 
#     if wt[i] > W:
#         ans = knapsack(W,val,wt,n,i+1)
#     else:
#         # inclusion of i th item 
#         ans1 = val[i]+knapsack(W-wt[i],val,wt,n,i+1)
#         # exclusion of i th item
#         ans2 = knapsack(W,val,wt,n,i+1)
#         ans = max(ans1,ans2)
#     return ans
    
# iterative model by bottomup model 
from sys import stdin
def knapsack(W,val,wt):
    n = len(val)
    dp = [[0 for j in range(W+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            if j < wt[i-1]:
                ans = dp[i-1][j]
            else:
                ans1 = val[i-1]+dp[i-1][j-wt[i-1]]
                ans2 = dp[i-1][j]

                ans = max(ans1,ans2)
            dp[i][j] = ans
    return dp[n][W]


def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), list(), n, 0

    weights = list(map(int, stdin.readline().rstrip().split(" ")))
    values = list(map(int, stdin.readline().rstrip().split(" ")))
    maxWeight = int(stdin.readline().rstrip())

    return maxWeight,values,weights 


#main
maxWeight,values,weights = takeInput()
print(knapsack(maxWeight,values,weights ))


# val = [200,300,100]
# wt = [20,25,30]
# W = 50
# ans = knapsack(W,val,wt)
# print(ans)