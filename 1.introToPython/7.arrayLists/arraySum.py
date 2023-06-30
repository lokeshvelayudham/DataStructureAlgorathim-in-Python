arr = [int(x) for x in input().split()]
#Printing the array/list
def printList(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i], end=" ")
    print()

printList(arr)