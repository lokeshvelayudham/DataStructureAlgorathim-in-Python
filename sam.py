from sys import stdin
def unique(arr,n):
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

def printL(arr,n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

    pass


def takeInput():
    n = int(stdin.readline().rstrip())
    
    if n == 0:
        return list(),0
    arr = list(map(int,stdin.readline().rstrip().split(" ")))
    return arr, n
    
    
t = int(stdin.readline().rstrip())
while t > 0:
    arr, n = takeInput()
   
    print(unique(arr,n))
    t -= 1