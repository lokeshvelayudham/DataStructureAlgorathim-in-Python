#code is contributed by Lokesh Poluru Velayudham


def palindrome(s):
    l = len(s)
    if l < 2:
        return True
    elif s[0] == s[l-1]:
        return palindrome(s[1:l-1])
    else:
        return False


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

s = input()
if palindrome(s):
    print("true")
else:
    print("false")