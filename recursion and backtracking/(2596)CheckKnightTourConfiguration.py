
class Solution(object):

    def checkValidGrid(self, grid):

        n = len(grid)

        moves = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]

        def solve(row, col, expected):

            if (row < 0 or row >= n or
                col < 0 or col >= n):
                return False

            if grid[row][col] != expected:
                return False

            if expected == n * n - 1:
                return True

            for dr, dc in moves:

                if solve(row + dr, col + dc, expected + 1):
                    return True

            return False

        return solve(0, 0, 0)
    


grid = [[0,3,6],[5,8,1],[2,7,4]]
print(Solution().checkValidGrid(grid))