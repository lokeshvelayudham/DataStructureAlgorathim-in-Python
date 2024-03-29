def getString(d):
    if d == 2:
        return "abc"
    if d == 3:
        return "def"
    if d == 4:
        return "ghi"
    if d == 5:
        return "jkl"
    if d == 6:
        return "mno"
    if d == 7:
        return "pqrs"
    if d == 8:
        return "tuv"
    if d == 9:
        return "wxyz"
    return " "

def keypad(n):
    if n == 0:
        output = []
        output.append("")
        return output
    
    smallerNumber = n//10
    lastDigit = n % 10

    smallerOutput = keypad(smallerNumber)
    optionForLastDigit = getString(lastDigit)

    output = []

    for s in smallerOutput:
        for c in optionForLastDigit:
            option = s + c
            output.append(option)
    return output
    
n = int(input())
ans = keypad(n)
for s in ans:
    print(s)