def printPathHelper(row,n,board):
    

def printPaths(n):
    board = [[0 for j in range(n)]for i in range(n)]
    printPathHelper(0,n,board)



n = int(input())
printPaths(n)
