#code is contributed by Lokesh Poluru Velayudham

n = int(input())
fH = (n+1) // 2
sH = n // 2
#first Half
for i in range(1,fH+1):
    #space
    for sp in range(fH-i,0,-1):
        print(" ",end="")
    #print *
    for st in range((2*i)-1):
        print("*",end="")
    print()

# second half
for i in range(sH,0,-1):
    #space 
    for sp in range(sH-i+1):
        print(" ",end="")
    #star
    for st in range((2*i)-1,0,-1):
        print("*",end="")
    print()