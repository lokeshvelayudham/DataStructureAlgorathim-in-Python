import math

def isSquare(x):
    s = int(math.sqrt(x))
    return s*s == x


def checkMember(n):
    return isSquare(5*n*n + 4) or isSquare(5*n*n - 4)
#Implement Your Code Here


n = int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
