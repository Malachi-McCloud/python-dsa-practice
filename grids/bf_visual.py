import matplotlib.pyplot as plt
from collections import deque
import numpy as np
import time

# Define the grid
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

rows, cols = len(grid), len(grid[0])
visited = [[False]*cols for _ in range(rows)]
queue = deque()

# Directions: up, down, left, right
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# Find starting point
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 1:
            queue.append((r, c))
            visited[r][c] = True

# Convert visited to numpy array for visualization
def get_visual_matrix():
    vis_matrix = np.zeros((rows, cols))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                vis_matrix[r][c] = 0.5  # Start cell
            elif visited[r][c]:
                vis_matrix[r][c] = 1.0  # Visited
    return vis_matrix

# Setup plot
plt.ion()
fig, ax = plt.subplots()
img = ax.imshow(get_visual_matrix(), cmap='Blues', vmin=0, vmax=1)
plt.title("BFS Grid Traversal")

# BFS loop with live updates
while queue:
    r, c = queue.popleft()

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if not visited[nr][nc] and grid[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = True

    img.set_data(get_visual_matrix())
    plt.draw()
    plt.pause(0.5)

plt.ioff()
plt.show()
