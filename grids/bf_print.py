from collections import deque
import time

# define the grid
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

rows, cols = len(grid), len(grid[0])
visited = [[False]*cols for _ in range(rows)]
queue = deque()

# Directions: up, down, left and right
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# Find the starting point
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 1:
            queue.append((r,c))
            visited[r][c] = True


def print_grid():
    for r in range(rows):
        row = ""
        for c in range(cols):
            if visited[r][c]:
                row += " V "
            elif grid[r][c] == 1:
                row += " S "
            else:
                row += " . "
        print(row)
    print()

# BFS visual logging
while queue:
    r, c = queue.popleft()
    print(f"Visiting {r}, {c}")
    print_grid()
    time.sleep(0.5) # pause for the visual effect


    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if not visited[nr][nc] and grid[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = True