def find_starting_cell(matrix, grade):
    n = len(matrix)
    
    # Define the possible neighbor directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    starting_row = float('inf')
    starting_col = float('inf')
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == grade:
                for dx, dy in directions:
                    new_row, new_col = i + dx, j + dy
                    
                    if 0 <= new_row < n and 0 <= new_col < n and matrix[new_row][new_col] == grade:
                        starting_row = min(starting_row, new_row)
                        starting_col = min(starting_col, new_col)
    
    if starting_row == float('inf') or starting_col == float('inf'):
        return -1, -1
    
    return starting_row, starting_col


# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the input for each test case
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    grade = int(input())
    
    # Find the starting cell of the connected group
    starting_row, starting_col = find_starting_cell(matrix, grade)
    
    # Print the result
    print(starting_row, starting_col)
