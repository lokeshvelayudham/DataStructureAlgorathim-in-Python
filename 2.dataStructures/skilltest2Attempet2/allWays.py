from sys import stdin , setrecursionlimit
setrecursionlimit(10**8)

def power(num, n):
 
    if(n == 0):
        return 1
    elif(n % 2 == 0):
        return power(num, n // 2) * power(num, n // 2)
    else:
        return num * power(num, n // 2) * power(num, n // 2)
 
# Function to check power representations recursively
 
 
def checkRecursive(x, n, curr_num=1, curr_sum=0):
 
    # Initialize number of ways to express
    # x as n-th powers of different natural
    # numbers
    results = 0
 
    # Calling power of 'i' raised to 'n'
    p = power(curr_num, n)
    while(p + curr_sum < x):
 
        # Recursively check all greater values of i
        results += checkRecursive(x, n, curr_num + 1, p + curr_sum)
        curr_num = curr_num + 1
        p = power(curr_num, n)
 
    # If sum of powers is equal to x
    # then increase the value of result.
    if(p + curr_sum == x):
        results = results + 1
 
    # Return the final result
    return results





# Main
a,b = [int(x) for x in stdin.readline().strip().split()] 
print(checkRecursive(a,b))