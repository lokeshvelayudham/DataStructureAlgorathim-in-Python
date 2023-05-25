def dfs(node, graph, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)

def find_special_walk(graph, n):
    visited = [False] * (n+1)
    special_walk = [0] * (n+1)

    for node in range(1, n+1):
        if not visited[node]:
            dfs(node, graph, visited)
            special_walk[node] = 1

    return special_walk[1:]

# Read input
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

# Find special walks
special_walks = find_special_walk(graph, n)

# Print the results
print(' '.join(map(str, special_walks)))
