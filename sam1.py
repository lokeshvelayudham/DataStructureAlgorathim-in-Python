n = int(input())  # 5
fH = (n+1)//2  # 3
sH = n//2  # 2
#firstHalf
i = 1
while i <= fH:
    #space
    space = 1
    while space <= fH-i:
        print(' ', end="")
        space = space+1
    #star
    star = 1
    while star <= (2*i)-1:
        print("*", end="")
        star = star+1
    print()
    i = i+1

#secondHalf
i = sH
while i >= 1:
    #space
    space = 1
    while space <= (sH-i+1):
        print(' ', end="")
        space = space+1
    #star
    star = 1
    while star <= (2*i)-1:
        print("*", end="")
        star += 1
    print()
    i -= 1
