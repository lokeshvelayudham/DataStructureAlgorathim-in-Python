import collections
inp_ls = list(map(int, input().split()))
itr = 0
queue = collections.deque()
n = 0
while inp_ls[itr]!=-1:
    choice = inp_ls[itr]
    if(choice==1):
        itr = itr+1
        if(n<=9):
            queue.appendleft(inp_ls[itr])
            n += 1
        else:
            print(-1)
    elif(choice==2):
        itr = itr+1
        if(n<=9):
            queue.append(inp_ls[itr])
            n += 1
        else:
            print(-1)
    elif(choice==3):
        if(n>=1):
            queue.popleft()
            n -= 1
        else:
            print(-1)
    elif(choice==4):
        if(n>=1):
            queue.pop()
            n -= 1
        else:
            print(-1)
    elif(choice==5):
        if(n>=1):
            element = queue.popleft()
            print(element)
            queue.appendleft(element)
        else:
            print(-1)
    elif(choice==6):
        if(n>=1):
            element = queue.pop()
            print(element)
            queue.append(element)
        else:
            print(-1)
    itr =itr + 1