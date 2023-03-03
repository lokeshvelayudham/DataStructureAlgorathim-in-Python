#code is contributed by Lokesh Poluru Velayudham

n = int(input())
i = 1
while i <= n:
    #spaces
    space = 1
    while space <= n-i:
        print(' ', end="")
        space += 1
    # numbers
    p = 1
    j = i
    while p <= i:
        print(j, end="")
        j -= 1
        p += 1
    #inverted
    k = 1
    j += 2
    while k < i:
        print(j, end="")
        k += 1
        j += 1
    print()
    i += 1
