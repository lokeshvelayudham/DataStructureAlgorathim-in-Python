#code is contributed by Lokesh Poluru Velayudham


from sys import stdin

def rowWiseSum(mat, nRows, mCols):
    sum = []
    for row in mat:
        s = 0
        for ele in row:
            s = s + ele
        sum.append(s)
    return sum


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
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    l= rowWiseSum(mat, nRows, mCols)
    print(*l)

    t -= 1