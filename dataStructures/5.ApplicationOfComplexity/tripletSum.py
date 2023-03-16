from sys import stdin

def tripletSum(arr,n,sum):
    arr.sort()
    trip_count=0
    for i in range(n):
        pair_sum=sum-arr[i]
        pair_count=pairSum(arr,i+1,n-1,pair_sum)
        trip_count+=pair_count
       
    return trip_count

def pairSum(arr,s,e,pair_sum):
    pair_count=0
    while s<e:
        if(arr[s]+arr[e]<pair_sum):
            s=s+1
        elif(arr[s]+arr[e]>pair_sum):
            e=e-1
        else:
            if(arr[s]==arr[e]):
                total_ele=(e-s)+1
                pair_count=pair_count+(total_ele*(total_ele-1)//2)
               
                return pair_count
           
            temp_s=s+1
            temp_e=e-1
            while((temp_s<=temp_e) and (arr[temp_s] == arr[s])):
                temp_s+=1
               
            while((temp_e>=temp_s) and (arr[temp_e] == arr[e])):
                temp_e-=1
               
            total_start=temp_s-s
            total_end=e-temp_e
            pair_count=pair_count+(total_start*total_end)
            s=temp_s
            e=temp_e
           
    return pair_count
#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
   
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(tripletSum(arr, n, num))

    t -= 1