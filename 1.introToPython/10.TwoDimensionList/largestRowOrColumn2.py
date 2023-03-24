'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

#code is contributed by Lokesh Poluru Velayudham


from sys import stdin

def findLargest(arr, nRows, mCols):
    sumRow = [0] * nRows
    sumCol = [0] * mCols
    for i in range(nRows):
        for j in range(mCols): 
            sumRow[i] += arr[i][j]
            sumCol[j] += arr[i][j] # Assume row 0 has maximum sum 
    l = ['row', 0, sumRow[0]]
    for i in range(nRows):
        if sumRow[i] > l[2]:
            l[2] = sumRow[i] 
            l[1] = i
    for j in range(mCols):
        if sumCol[j] > l[2]:
            l[2] = sumCol[j] 
            l[1] = j 
            l[0] = 'column' 
    return l


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
    l = findLargest(mat, nRows, mCols)
    print(*l)

    t -= 1