from sys import stdin

def pairSum0(arr,n):
    unordered_map = {}
    count = 0
    sum = 0
    for i in range(n):
        if sum - arr[i] in unordered_map:
            count += unordered_map[sum - arr[i]]
        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1
    return count
 

def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))