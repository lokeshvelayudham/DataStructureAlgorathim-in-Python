from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


def getCompressedString(s) :
	# Write your code here.
    res = ""
    count = 1
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            count +=1
        else:
            res += s[i-1]
            if count > 1:
                res += str(count)
            count = 1
    res = res + s[-1]
    if count > 1:
      res += str(count)
    return res




# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)