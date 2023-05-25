from collections import defaultdict

def count_tuples(nums):

    ans = 0
    freq = {}
    for i in range(len(nums)):
        for j in range(i+1, len(nums)): 
            key = nums[i] * nums[j]
            ans += freq.get(key, 0)
            freq[key] = 1 + freq.get(key, 0)
    return 8*ans

# Read input
N = int(input())
nums = list(map(int, input().split()))

# Call the function and print the result
result = count_tuples(nums)
print(result)
