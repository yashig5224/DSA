class Solution(object):

    def findPath(self, maze):

        n = len(maze)

        ans = []

        visited = [[False] * n for _ in range(n)]

        def solve(row, col, path):

            if (row < 0 or row >= n or
                col < 0 or col >= n):
                return

            if maze[row][col] == 0:
                return

            if visited[row][col]:
                return

            if row == n - 1 and col == n - 1:
                ans.append(path)
                return

            visited[row][col] = True

            solve(row + 1, col, path + "D")

            solve(row, col - 1, path + "L")

            solve(row, col + 1, path + "R")

            solve(row - 1, col, path + "U")

            visited[row][col] = False

        if maze[0][0] == 1:
            solve(0, 0, "")

        return ans