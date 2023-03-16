from sys import stdin


def findDuplicate(arr, n) :
    dic={}                 
    for i in arr:          
        dic[i]=0  
        # print(dic)           
    for i in arr:
        dic[i] +=1
        # print(dic)
    for i in arr:         
        if dic[i] ==2:    
           return i
 
    #Your code goes here




#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip()) 

while t > 0 :

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1