from os import *
from sys import *
from collections import *
from math import *


def checkArm(n):
    x = n
    l = len(str(n))
    s = 0
    while n != 0:
        b = n % 10
        s = s + (b**l)
        n = n // 10
    return(s == x)


n = int(input())
isArm = checkArm(n)
if(isArm):
    print("true")
else:
    print("false")
