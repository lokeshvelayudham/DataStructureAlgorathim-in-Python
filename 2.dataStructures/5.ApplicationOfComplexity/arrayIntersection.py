#code is contributed by Lokesh Poluru Velayudham
# Time = O(nlogn)

from sys import stdin
import sys


def merge(a1,a2,a):
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a[k] = a1[i]
            k+=1
            i+=1
        else:
            a[k] = a2[j]
            k+=1
            j+=1
    
    while i < len(a1):
        a[k] = a1[i]
        k+=1
        i+=1
    while j < len(a2):
        a[k] = a2[j]
        k+=1
        j+=1
    return a


def mergesort(a):
    if len(a) == 0 or len(a) == 1:
        return
    mid =len(a)//2
    a1 = a[0:mid]
    a2 = a[mid:]

    mergesort(a1)
    mergesort(a2)
    merge(a1,a2,a)
    return a
def intersectionOfSorted(arr1,arr2,n,m):
     i, j = 0, 0
     while i < n and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j+= 1
        else:
            print(arr2[j],end=" ")
            j += 1
            i += 1


def intersection(arr1, arr2, n, m) :
    mergesort(arr1)
    mergesort(arr2)
    intersectionOfSorted(arr1,arr2,n,m)
    # i, j = 0, 0
    # while i < n and j < m:
    #     if arr1[i] < arr2[j]:
    #         i += 1
    #     elif arr2[j] < arr1[i]:
    #         j+= 1
    #     else:
    #         print(arr2[j],end=" ")
    #         j += 1
            # i += 1
 
 



# Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
    	return list(), 0
    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()
    intersection(arr1, arr2, n, m)
    print()

    t -= 1