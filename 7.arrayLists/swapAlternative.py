#code is contributed by Lokesh Poluru Velayudham


from sys import stdin


def swapAlternate(arr, n):
    length = len(arr)
    i = 0
    for j in range(n//2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 2
    pass
    #Your code goes here

#Taking Input Using Fast I/O


def takeInput():
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#Printing the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    if n != 0:
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1
