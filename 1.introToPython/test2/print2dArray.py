from os import *
from sys import *
from collections import *
from math import *
from sys import stdin




#code is contributed by Lokesh Poluru Velayudham



def print2darray(mat, nRows, mCols):
    for i in range(nRows):
        n = nRows-i
        while n != 0:
            for j in range(mCols):
            # for k in range(nRows,1,-1):
                print(mat[i][j],end=" ")
            print()
            n-=1
        # print()



#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
# t = int(stdin.readline().rstrip())

# while t > 0 :

mat, nRows, mCols = take2DInput()
print2darray(mat, nRows, mCols)

    # t -= 1





