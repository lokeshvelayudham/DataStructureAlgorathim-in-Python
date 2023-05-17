#code is contributed by Lokesh Poluru Velayudham

from sys import stdin
def printMatrixDiagonal(mat,n,m):
	for k in range(m):
		i = k
		j = 0
	while i >= 0 and j < n:
		print(mat[i][j], end=" ")
		i -= 1
		j += 1

	for k in range(1, n):
		i = m - 1
		j = k
	while j < n and i >= 0:
		print(mat[i][j], end=" ")
		i -= 1
		j += 1



li = stdin.readline().rstrip().split(" ")
nRows = int(li[0])
mCols = int(li[1])


mat = []
for i in range(nRows):
	row = stdin.readline().rstrip().split(" ")
	mat.append(row)
	
# mat = [map(int, input().strip().split(" ")) for row in range(nRows)]
    # return mat, nRows, mCols




printMatrixDiagonal(mat,nRows,mCols)