def find_character(N, X):
    if N == 1:
        return "0" if X == 1 else "1"
    
    mid = 2**(N-1)
    if X <= mid:
        return find_character(N-1, X)
    else:
        return "1" if find_character(N-1, X-mid) == "0" else "0"

# Taking input
T = int(input())

for _ in range(T):
    N, X = map(int, input().split())

    # Calling the function
    result = find_character(N, X)
    print(result)
