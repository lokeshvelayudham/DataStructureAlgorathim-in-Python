#code is contributed by Lokesh Poluru Velayudham

from sys import stdin


def isPermutation(string1, string2):
    l1 = len(string1)
    l2 = len(string2)
    if l1 == l2:
        #sorted
        a = sorted(string1)
        b = " ".join(a)
        c = sorted(string2)
        d = " ".join(c)
        if b == d:
            return True

    return False
#Your code goes here


#main
string1 = stdin.readline().strip()
string2 = stdin.readline().strip()

ans = isPermutation(string1, string2)

if ans:
    print('true')
else:
    print('false')
