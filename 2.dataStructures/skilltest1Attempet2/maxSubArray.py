def max_subarray_sum(arr):
    max_sum = arr[0]  # Initialize max_sum with the first element
    curr_sum = arr[0]  # Initialize curr_sum with the first element

    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum

n = int(input())
arr = list(map(int, input().split()))
print(max_subarray_sum(arr))