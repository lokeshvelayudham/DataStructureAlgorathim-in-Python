#code is contributed by Lokesh Poluru Velayudham

import sys

def findUnique(arr, n) :
    for i in range(n):
        j = 0
        while j < n:
        # for j in range(n+1):
            if i != j:
                if arr[i] == arr[j]:
                    break
            j+=1
        if j == n:
            return (arr[i])

    pass
    #Your code goes here

#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1