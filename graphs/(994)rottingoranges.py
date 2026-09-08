from collections import deque

class Solution:
    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])

        q = deque()
        visited = [[False] * m for _ in range(n)]

        fresh = 0

        # Put all rotten oranges into queue
        for i in range(n):
            for j in range(m):

                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited[i][j] = True

                elif grid[i][j] == 1:
                    fresh += 1

        directions = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

        max_time = 0

        # Multi-source BFS
        while q:
            r, c, time = q.popleft()

            max_time = max(max_time, time)

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < n and
                    0 <= nc < m and
                    grid[nr][nc] == 1 and
                    not visited[nr][nc]):

                    visited[nr][nc] = True
                    fresh -= 1

                    q.append((nr, nc, time + 1))

        # Fresh oranges still remaining
        if fresh > 0:
            return -1

        return max_time
    
    
    
#general multisource bfs template
from collections import deque

def multi_source_bfs(grid):
    if not grid or not grid[0]:
        return
    
    rows, cols = len(grid), len(grid[0])
    q = deque()
    visited = set()

    # 1. Add ALL sources
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "source":  # Replace "source" with your source condition (e.g., grid[r][c] == 1)
                q.append(((r, c), 0))
                visited.add((r, c))

    # 2. Process BFS Queue
    while q:
        (r, c), time = q.popleft()

        # Explore 4-directional neighbors (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            # Check if neighbor is within bounds and not visited
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                # Add any custom condition here (e.g., if grid[nr][nc] != obstacle)
                visited.add((nr, nc))
                q.append(((nr, nc), time + 1))    