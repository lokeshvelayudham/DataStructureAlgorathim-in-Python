from os import *
from sys import *
from collections import *
from math import *

def breakNumber(n):
    # Write your code here.
    arr = list(range(1, n + 1))
    res = []

    def backtrack(idx, target, tmp):
        if target == 0:
            res.append(tmp[:])
            return
        
        if idx == n or target < 0:
            return
        
        for i in range(idx, len(arr)):
            tmp.append(arr[i])
            backtrack(i, target - arr[i], tmp)
            tmp.pop()
 
    backtrack(0, n, [])
    return res

n = int(input())
ans = breakNumber(n)
for i in ans:
    nAns = i
    nA = ""
    for j in nAns:
        nA += str(j)+ " "
    print(nA)
    # print(str(nAns))
    # print(type(nAns))
    