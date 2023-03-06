def binary(a,x,si,ei):
    if si > ei:
        return -1
    mid = si + ei // 2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary(a,x,si,mid-1)
    else:
        return binary(a,x,mid+1,ei)

a = list(map(int, input().strip().split()))
x = int(input())
si = 0 
ei = len(a)
print(binary(a,x,si,ei))
