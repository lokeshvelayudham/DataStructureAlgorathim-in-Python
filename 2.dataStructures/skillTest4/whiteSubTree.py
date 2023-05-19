def dfs(node, parent, colors, white_count, black_count, max_diff, graph):
    # Update white and black counts based on the color of the current node
    if colors[node] == 1:
        white_count += 1
    else:
        black_count += 1

    # Calculate the difference between white and black counts
    diff = white_count - black_count

    # Update the maximum difference if needed
    max_diff[node] = diff

    # Traverse the adjacent nodes
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, colors, white_count, black_count, max_diff, graph)

    # Backtrack and remove the current node's count
    if colors[node] == 1:
        white_count -= 1
    else:
        black_count -= 1

def calculate_max_diff(T, test_cases):
    results = []

    for _ in range(T):
        N, colors, edges = test_cases[_]

        # Create an adjacency list to represent the tree
        graph = [[] for _ in range(N + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize arrays to store white and black counts, and maximum differences
        white_count = [0] * (N + 1)
        black_count = [0] * (N + 1)
        max_diff = [0] * (N + 1)

        # Perform DFS for each vertex to calculate maximum differences
        dfs(1, 0, colors, white_count, black_count, max_diff, graph)

        results.append(max_diff[1:])

    return results

# Read the input
T = int(input())
test_cases = []

for _ in range(T):
    N = int(input())
    colors = list(map(int, input().split()))
    edges = []
    for _ in range(N - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    test_cases.append((N, colors, edges))

# Calculate the maximum differences for each test case
results = calculate_max_diff(T, test_cases)

# Print the results
for res in results:
    print(*res)
