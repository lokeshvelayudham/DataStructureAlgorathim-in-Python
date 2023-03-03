# n =int(input())
# x = str(n)
# # temp = n
# # rev = 0
# # while(n > 0):
# r = x[::-1]
# if r == x:
#     # print(r)
#     # print(x)
#     print (True)
# else:
#     # print(r)
#     # print(x)
#     print(False)

#code is contributed by Lokesh Poluru Velayudham




num=int(input())
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("true")
else:
    print("false")

