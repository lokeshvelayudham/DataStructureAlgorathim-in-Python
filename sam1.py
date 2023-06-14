n = int(input())
fH = (n+1)//2
sH = n//2
#firsthalf
i = 1
while i <= fH:
    #space
    space = 1
    while space < i:
        print(" ", end="")
        space += 1
    #stars
    star = 1
    while star <= i:
        print("*", end=" ")
        star += 1
    print()
    i += 1
#secondhalf
j = sH
while j >= 1:
    #space
    space = 1
    while space < j:
        print(" ", end="")
        space += 1
    #stars
    star = 1
    while star <= j:
        print("*", end=" ")
        star += 1
    print()
    j -= 1
