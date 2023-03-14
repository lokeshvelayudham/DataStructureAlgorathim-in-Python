# Problem: Remove x from string
def removeX(string):
    l = len(string)
    if l == 0:
        return string
    smallOutput = removeX(string[1:])
    if string[0] == 'x':
        return "" + smallOutput
    else:
        return string[0] + smallOutput
    pass

# Main
string = input()
print(removeX(string))
