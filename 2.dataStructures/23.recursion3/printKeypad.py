def printKeypadHelper(num, str):
    options = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    if (num==0):
        print(str)
        return;

    small = num//10
    remainder = num%10
    optionslen = len(options[remainder])
    if(optionslen==0):
        printKeypadHelper(small, str)
        return

    for i in range(0, optionslen):
        printKeypadHelper(small, options[remainder][i] + str)

def printKeypad(num):
    printKeypadHelper(num,"")

n=int(input())
printKeypad(n)