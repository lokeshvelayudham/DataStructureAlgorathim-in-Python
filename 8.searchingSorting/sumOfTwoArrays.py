from sys import stdin


def sumOfTwoArrays(arr1, n, arr2, m, output):
    i = n-1
    j = m-1
    c = 0
    k = max(n, m)
    while i >= 0 and j >= 0:
        sum = arr1[i]+arr2[j]+c
        output[k] = sum % 10
        c = sum // 10
        i -= 1
        j -= 1
        k -=1
    while i >= 0:
        sum = arr1[i]+c
        output[k] = sum % 10
        c = sum // 10
        i -= 1
        k -= 1
    while j >= 0:
        sum = arr2[j]+c
        output[k] = sum % 10
        c = sum // 10
        j -= 1
        k -= 1
    output[0] = c
    # es here


#Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()

    outputSize = (1 + max(n, m))
    output = outputSize * [0]

    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)

    t -= 1