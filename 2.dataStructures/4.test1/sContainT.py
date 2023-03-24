#code is contributed by Lokesh Poluru Velayudham

def contains(s,t):
    if len(t) == 0:
        return True
    if len(s) == 0:
        return False
    
    if(s[0] == t[0]):
        return contains(s[1:],t[1:])
    else:
        return contains(s[1:],t)
    


s = input()
t = input()
ans = contains(s,t)
if ans is True:
    print("true")
else:
    print("false")