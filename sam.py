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
        outPut = []
        outPut.append("")
        return outPut
    smallerNumber = n // 10
    lastDigit = n % 10

    smallerOutput = keypad(smallerNumber)
    option = getString(lastDigit)

    outPut = []
    for s in smallerOutput:
        for c in option:
            outPut.append(s + c)
    return outPut



n = int(input())
ans = keypad(n)
for ele in ans:
    print(ele)