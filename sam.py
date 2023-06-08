n = int(input())
i = 0
while i < n:
    j = 0
    while j < n:
        if j == i:
            print("*",end="")
        else:
            print(0,end="")
        print("*",end="")
        j += 1
        p = n
    while j > 0:
        if j == i+1:
            print("*",end="")
        else:
            print(0,end="")

        j -= 1
    print()

    i += 1