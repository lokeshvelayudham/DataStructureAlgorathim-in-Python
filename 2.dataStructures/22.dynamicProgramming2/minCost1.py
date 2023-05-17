#code is contributed by Lokesh Poluru Velayudham


# import sys
# def minCost(cost,i,j,n,m,dp):
#     # special case
#     if  i == n-1 and j == m-1:
#         return cost[i][j]
    
#     # base case
#     if  i >= n or j >= m:
#         return sys.maxsize

#     if dp[i][j+1] == sys.maxsize:
#         ans1 = minCost(cost,i,j+1,n,m,dp)
#         dp[i][j+1] = ans1
#     else:
#        ans1 = dp[i][j+1] 
    
#     if dp[i+1][j] == sys.maxsize:
#         ans2 = minCost(cost,i+1,j,n,m,dp)
#         dp[i+1][j] = ans2
#     else:
#        ans2 = dp[i+1][j] 
    
#     if dp[i+1][j+1] == sys.maxsize:
#         ans3 = minCost(cost,i+1,j+1,n,m,dp)
#         dp[i+1][j+1] = ans3
#     else:
#        ans3 = dp[i+1][j+1] 

    

#     ans = cost[i][j] + min(ans1,ans2,ans3)
#     return ans

# cost = [[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
# n = 4
# m = 3
# dp = [[sys.maxsize for j in range(m+1)]for i in range(n+1)]
# ans = minCost(cost,0,0,4,3,dp)
# print(ans)


# iterative solution after memozation :
import sys
from sys import stdin
def minCostPath(mat, mRows, nCols):
    dp = [[sys.maxsize for j in range(nCols+1)]for i in range(mRows+1)]
    for i in range (mRows-1,-1,-1):
        for j in range (nCols-1,-1,-1):
            if i == mRows-1 and j == nCols-1:
                dp[i][j] = mat[i][j]
            else:
                ans1 = dp[i+1][j]
                ans2 = dp[i][j+1]
                ans3 = dp[i+1][j+1]
                dp[i][j] = mat[i][j] + min(ans1,ans2,ans3)
    
    return dp[0][0]

    
# cost = [[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
# n = 4
# m = 3
# ans = minCostIter(cost,n,m)
# print(ans)

def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])
    
    if mRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


#main
mat, mRows, nCols = take2DInput()
print(minCostPath(mat, mRows, nCols))