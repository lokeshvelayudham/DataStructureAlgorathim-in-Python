def find_lexicographically_smallest(S, queries):
    result = []

    for query in queries:
        X, CODE = query

        # Select the subset of strings from S1 to SX
        selected_strings = S[:X]

        # Find the longest common prefix length with CODE
        max_prefix_length = 0
        for string in selected_strings:
            prefix_length = 0
            while prefix_length < len(CODE) and prefix_length < len(string) and CODE[prefix_length] == string[prefix_length]:
                prefix_length += 1
            max_prefix_length = max(max_prefix_length, prefix_length)

        # Find all strings with the maximum prefix length
        max_prefix_strings = []
        for string in selected_strings:
            if len(string) >= max_prefix_length and string[:max_prefix_length] == CODE[:max_prefix_length]:
                max_prefix_strings.append(string)

        # Find the lexicographically smallest string
        min_string = min(max_prefix_strings)

        result.append(min_string)

    return result

# Read input
n = int(input())
S = []
for _ in range(n):
    string = input()
    S.append(string)

q = int(input())
queries = []
for _ in range(q):
    X, CODE = input().split()
    X = int(X)
    queries.append((X, CODE))

# Call the function and print the result
result = find_lexicographically_smallest(S, queries)
for string in result:
    print(string)
