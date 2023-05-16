#code is contributed by Lokesh Poluru Velayudham


from sys import stdin
from sys import maxsize as MAX_VALUE

def countMinSteps(n):
    if n == 1:
        return 0
    
    minSteps = [0] * (n+1)
    minSteps[1] = 0

    for i in range(2,(n+1)):
        subOne = MAX_VALUE
        div2 = MAX_VALUE
        div3 = MAX_VALUE

        subOne = minSteps[i-1]

        if i % 2 == 0:
            div2 = minSteps[i//2]
        
        if i % 3 == 0:
            div3 = minSteps[i//3]

        minSteps[i] = 1 + min(subOne,div2,div3)
    return minSteps[n]

#main
n = int(stdin.readline().rstrip())
print(countMinSteps(n))