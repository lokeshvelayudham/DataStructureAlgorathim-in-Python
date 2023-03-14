#code is contributed by Lokesh Poluru Velayudham

def split(arr,n,i,fsum,tsum):
    # reached end
    if (i == n):
        return fsum == tsum
    
    # divisible by 5
    if(arr[i] % 5 == 0):
        fsum += arr[i]
    # divisilbe by 3
    elif(arr[i] % 3 == 0):
        tsum += arr[i]
    # added to any substring
    else:
        return (split(arr,n,i+1,fsum+arr[i],tsum) or
                split(arr,n,i+1,fsum,tsum+arr[i]))
    return split(arr,n,i+1,fsum,tsum)

   
    
x = input()
arr = [int(ele) for ele in input().split()]
n = len(arr)
ans = split(arr,n,0,0,0)
if ans is True:
    print('true')
else:
    print('false')