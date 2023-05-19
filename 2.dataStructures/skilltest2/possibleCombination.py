import itertools

N = int(input())
numbers = list(map(int, input().split()))

# Generate all combinations of choosing 12 numbers
combinations = list(itertools.combinations(numbers, 12))

# Print the combinations in sorted order
for comb in combinations:
    print(*comb)