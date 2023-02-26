n = int(input())
#fisthalf
i = 1
while i <= n:
    #spaces
    space = 1
    while space < i:
        print(" ", end="")
        space += 1
    #numvbers

    j = 1
    p = i
    # j+=1
    while j <= n-i+1:
        print(p, end="")
        j += 1
        p += 1

    print()
    i += 1
#second half
for x in range(n-1, 0, -1):
    c = 1
    for y in range(1, x):
        print(" ", end="")
        c = c+1
    num = x
    for y in range(c, n+1):
        print(num, end="")
        num += 1
    print()