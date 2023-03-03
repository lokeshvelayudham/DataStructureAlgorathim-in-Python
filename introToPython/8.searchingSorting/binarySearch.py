from typing import *

def binarySearch(arr : List[int], n : int, x : int) :
    
    start = 0
    end = n-1
    mid = start
    while start <= end:
        mid = start + (end-start) // 2
        if arr[mid] < x:
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            return mid
    return -1
    #Your code goes here
    pass
