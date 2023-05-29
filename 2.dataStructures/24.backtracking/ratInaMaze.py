def printPathHelp(x,y,maze,n,solu):
    if x == n-1 and y == n-1:
        solu[x][y] = 1
        print(solu)
        solu[x][y] = 0
        return
    if x < 0 or y < 0 or x >= n or y >= n or maze[x][y] == 0 or solu[x][y] == 1:
        return
    
    solu[x][y] = 1
    printPathHelp(x-1,y,maze,n,solu)
    printPathHelp(x,y-1,maze,n,solu)
    printPathHelp(x+1,y,maze,n,solu)
    printPathHelp(x,y+1,maze,n,solu)
    solu[x][y] = 0
    return
 
def printPath(maze):
    n = len(maze)
    solu = [[0 for i in range(n)]for j in range(n)]
    printPathHelp(0,0,maze,n,solu)

n = int(input())
maze = [] 
for i in range(n):
    row = [int(ele) for ele in input().split()]
    maze.append(row)
printPath(maze)