#code is contributed by Lokesh Poluru Velayudham


# partition

def partition(a, si, ei):
    p = a[si]
    c = 0
    for i in range(si,ei+1):
        if a[i] < p:
            c+=1
    a[si+c] , a[si] = a[si], a[si+c]
    pi = si+c

    i = si
    j = ei
    while i < j:
        if a[i] < p:
            i+=1
        elif a[j] >= p:
            j-=1
        else:
            a[i], a[j] = a[j], a[i]
            i+=1
            j-=1
    return pi


# QuickSort 

def quicksort(a, si, ei):
    if si >= ei:
        return
    pi = partition(a, si, ei)
    quicksort(a, si, pi-1)
    quicksort(a, pi+1, ei)

# To print Array
def printl(a):
    for i in range (len(a)):
        print(a[i],end=" ")
    print()

# Main
n = int(input())
a = list(map(int, input().strip().split()))
quicksort(a, 0 ,len(a)-1)
printl(a)