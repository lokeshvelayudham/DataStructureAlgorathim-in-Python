def replace(s, a, b):
    if len(s) == 0:
        return s
    
    smallOutput = replace(s[1:],a,b)
    if s[0] == a:
        return b + smallOutput
    else:
        return s[0] + smallOutput
    
# Main

s = input()
a = input()
b = input()
print(replace(s,a,b))