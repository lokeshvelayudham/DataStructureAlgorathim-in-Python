# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(s):
    # Please add your code here
    if len(s) == 1 :
        return s
    smallOutput = removeConsecutiveDuplicates(s[1:])
    if s[0] == s[1]:
        return "" + smallOutput
    else:
        return s[0] + smallOutput
    pass

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
