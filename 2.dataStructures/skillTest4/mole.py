def findMole(N, T, trust_relationships):
    # Count the trust levels of each agent
    trust_counts = [0] * (N + 1)  # Index 0 is not used

    for trust in trust_relationships:
        x, y = trust
        trust_counts[x] -= 1  # Agent x trusts someone
        trust_counts[y] += 1  # Agent y is trusted by someone

    # Find the agent who trusts nobody and is trusted by everyone else
    for i in range(1, N + 1):
        if trust_counts[i] == N - 1:
            return i

    return -1  # No mole found

# Read the input
N, T = map(int, input().split())
trust_relationships = []
for _ in range(T):
    x, y = map(int, input().split())
    trust_relationships.append((x, y))

# Find the mole
mole = findMole(N, T, trust_relationships)

# Print the result
print(mole)
