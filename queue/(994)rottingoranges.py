from collections import deque

class Solution(object):

    def orangesRotting(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0

        # Store all rotten oranges
        # Count fresh oranges
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 2:
                    q.append((r, c))

                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        # BFS
        while q and fresh > 0:

            size = len(q)

            for _ in range(size):

                r, c = q.popleft()

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    # Valid and fresh orange
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        fresh -= 1

                        q.append((nr, nc))

            minutes += 1

        if fresh == 0:
            return minutes

        return -1