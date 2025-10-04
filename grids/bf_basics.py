# Define a grid 1 = start point 0 = unvisited cells
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
    ]

# define directions
directions = [(-1, 0), (1,0), (0, -1), (0, 1)] # each tuple represents (row, col)


from collections import deque

# def bfs function passing our grid
def bfs(grid):
    rows, cols = len(grid), len(grid[0])
    visited =[[False for _ in range(cols)] for _ in range (rows)]
    queue = deque()

    # find the starting point
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                queue.append((r, c))
                visited[r][c] = True
                print(f"Start at ({r}, {c})")

    while queue:
        r, c = queue.popleft()
        print(f"Visiting ({r}, {c})")

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and grid[nr][nc] == 0:
                    queue.append((nr, nc))
                    visited[nr][nc] = True
                    print(f" -> Queued ({nr}, {nc})")

bfs(grid)
