def printTable(s,e,step):
    for i in range(s,e+1,step):
        c = (i-32)*5/9
        cf = int(c)
        print(i,cf)




s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)