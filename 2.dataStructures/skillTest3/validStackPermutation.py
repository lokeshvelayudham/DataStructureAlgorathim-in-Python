def isValidStackPermutation(first, other):
    stack = []  # Initialize an empty stack
    i = 0  # Index for the other array

    for num in first:
        stack.append(num)  # Push elements from the first array to the stack

        while stack and stack[-1] == other[i]:
            stack.pop()  # Pop elements from the stack that match the other array
            i += 1

    return len(stack) == 0  # Return True if the stack is empty (valid permutation), else False

# Taking input
T = int(input())

for _ in range(T):
    N = int(input())
    first = list(map(int, input().split()))
    other = list(map(int, input().split()))

    # Checking if first array is a valid stack permutation of the other
    if isValidStackPermutation(first, other):
        print("YES")
    else:
        print("NO")
