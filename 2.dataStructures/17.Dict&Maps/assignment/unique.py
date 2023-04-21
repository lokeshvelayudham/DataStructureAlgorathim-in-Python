def unique(s):
    ans =''
    d = {}
    for char in s:
        if char not in d:
            ans = ans + char
            # print(d)
            d[char] = True
    return ans


s = input()
print(unique(s))
