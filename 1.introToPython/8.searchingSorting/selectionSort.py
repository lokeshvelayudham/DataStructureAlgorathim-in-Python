#code is contributed by Lokesh Poluru Velayudham


from sys import stdin


def selectionSort(arr, n):
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr
    #Your code goes here

#Taking Input Using Fast I/O


def takeInput():
    n = int(stdin.readline().strip()) #length of array 
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" "))) #arrays
    return arr, n


#to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


#main
t = int(stdin.readline().strip()) #testcases

while t > 0:

    arr, n = takeInput() 
    selectionSort(arr, n)
    printList(arr, n)

    t -= 1
