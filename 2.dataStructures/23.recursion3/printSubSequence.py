def printSub(s,o):
    if len(s) == 0:
        print(o)
        return
    printSub(s[1:],o)
    printSub(s[1:],o+s[0])

s = input()
ans = printSub(s,"")
# print(ans)