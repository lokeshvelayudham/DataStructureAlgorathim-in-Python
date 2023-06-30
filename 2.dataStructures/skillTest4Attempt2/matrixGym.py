def dfs(grid, i, j, current_calories, target_calories, visited):
    rows = len(grid)
    cols = len(grid[0])
    
    # Check if current position is out of bounds or already visited
    if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j]:
        return False
    
    # Mark current cell as visited
    visited[i][j] = True
    
    # Check if the current cell is a hurdle ('#')
    if grid[i][j] == '#':
        return False
    
    # Update current calories burned
    current_calories += 5
    
    # Check if target calories reached
    if current_calories >= target_calories:
        return True
    
    # Explore neighboring cells (right and down)
    if dfs(grid, i, j+1, current_calories, target_calories, visited) or dfs(grid, i+1, j, current_calories, target_calories, visited):
        return True
    
    # Unmark current cell as visited (backtrack)
    visited[i][j] = False
    
    return False


def find_path(grid, target_calories):
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize visited matrix
    visited = [[False] * cols for _ in range(rows)]
    
    # Start DFS from top-left cell
    if dfs(grid, 0, 0, 0, target_calories, visited):
        # Calculate extra calories burned
        total_calories = sum(sum(row) for row in visited) * 5
        extra_calories = total_calories - target_calories
        return "Yes", extra_calories
    else:
        return "No"


# Read input
N = int(input())
grid = input().split()
calories = int(input())

# Call the function
result = find_path(grid, calories)

# Print the result
print(*result)

