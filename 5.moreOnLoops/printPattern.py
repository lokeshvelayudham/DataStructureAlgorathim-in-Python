n = int(input())
startValue = 1
for i in range(1, n+1):
    for j in range(startValue, startValue + n):
        print(j, end=" ")
    print()
    if(i == ((n+1)//2)):
        if((n % 2) != 0):
            startValue = n*(n-2)+1
        else:
            startValue = n*(n-1) + 1
    elif((i > (n+1)//2)):
        startValue = startValue - 2*n
    else:
        startValue = startValue + 2*n