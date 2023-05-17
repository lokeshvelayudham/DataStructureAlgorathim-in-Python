from sys import stdin
def count_ones_substrings(binary_str):
    count = 0
    current_count = 0

    for char in binary_str:
        if char == '1':
            current_count += 1
            count += current_count
        else:
            current_count = 0

    return count

# Test the function
t = int(stdin.readline().rstrip())

while t > 0 :
    binary_str = input()
    total_substrings = count_ones_substrings(binary_str)
    print(total_substrings)

    t -= 1
