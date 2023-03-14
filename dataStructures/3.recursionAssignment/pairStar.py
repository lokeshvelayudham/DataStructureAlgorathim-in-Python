#code is contributed by Lokesh Poluru Velayudham


def pairStar(i,o,n=0):

    # Append current character
    o = o + i[n]

    # if we reach last char
    if (n == len(i)-1):
        print(o)
        return
    
    if(i[n] == i[n+1]):
        o += "*"
    pairStar(i,o,n+1)
    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

i = input()
o = ""
pairStar(i,o)