'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

#code is contributed by Lokesh Poluru Velayudham


from sys import stdin

def findLargest(arr, nRows, mCols):
    isRow = True
    min_value_r = -2147483648
    min_value_c = -2147483648
    # row sum 
    for i in range(nRows):
        sum_row = 0
        # row_sums = 0
        for j in range(mCols):
            sum_row+=arr[i][j]
    # print(sum_row)


        if sum_row > min_value_r:
            min_value_r = sum_row
            max_row_index = i
    # print(min_value_r)


# colums sums

    for j in range(mCols):
        sum_cols = 0
        # cols_sums = 0
        for i in range(nRows):
            sum_cols += arr[i][j]
        # print(sum_cols)
            
        if sum_cols > min_value_c:
            min_value_c = sum_cols
            max_cols_index = j
            isRow = False
    # print(min_value_c)

    if isRow :
        print("row" + str(max_row_index)+" " + str(min_value_r))
    else:
        print("column"+ str(max_cols_index)+" "+ str(min_value_c))
        


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
    findLargest(mat, nRows, mCols)

    t -= 1