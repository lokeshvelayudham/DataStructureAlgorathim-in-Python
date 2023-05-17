n = int(input())

l = n
for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        print(n - j + 1, end='')
    if i > 1:
        for p in range(1, 2 * (i - 1) + 1):
            print("*", end='')
    for j in range(l, 0, -1):
        print(j, end='')
    l = l - 1
    print()
