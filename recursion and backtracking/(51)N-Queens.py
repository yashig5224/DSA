class Solution(object):

    def solveNQueens(self, n):

        board = [["."] * n for _ in range(n)]
        ans = []

        def isSafe(row, col):

            # Check column
            r = row
            while r >= 0:
                if board[r][col] == "Q":
                    return False
                r -= 1

            # Check left diagonal
            r = row
            c = col

            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            # Check right diagonal
            r = row
            c = col

            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True

        def solve(row):

            if row == n:    #If we have placed queens in all rows, we found one valid solution.
                temp = []    #Convert the board into the required format and save it in ans. Then stop this path and go back.
                 
                for r in board:
                    temp.append("".join(r))

                ans.append(temp)
                return

            for col in range(n):    #➡️ Try placing the queen in every column of the current row.

                if isSafe(row, col):   #➡️ Check if placing a queen at (row, col) is safe.

                    board[row][col] = "Q"    #Place the queen

                    solve(row + 1)         #➡️ Move to the next row and place the next queen.

                    # Backtrack
                    board[row][col] = "."   #Backtracking: Remove the queen so you can try another column in the current row.

        solve(0)   #Backtracking: Remove the queen so you can try another column in the current row.

        return ans