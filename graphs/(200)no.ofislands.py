class Solution:
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for _ in range(n)]
        count = 0

        def dfs(r, c):
            # Out of bounds
            if r < 0 or r >= n or c < 0 or c >= m:
                return

            # Water or already visited
            if grid[r][c] == "0" or visited[r][c]:
                return

            visited[r][c] = True

            # Up
            dfs(r - 1, c)

            # Right
            dfs(r, c + 1)

            # Down
            dfs(r + 1, c)

            # Left
            dfs(r, c - 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    count += 1
                    dfs(i, j)

        return count