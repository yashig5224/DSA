#linear search in 2d matrix -leetcode 74
class Solution(object):
    def searchMatrix(self, matrix, target):

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == target:
                    return True

        return False
    
#binary search in 2d matrix -leetcode 74
class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2

            value = matrix[mid // n][mid % n]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
    
    
#max row sum in 2d matrix
def maximum_row_sum(matrix):

    maximum = float("-inf")

    for row in matrix:

        total = sum(row)

        maximum = max(maximum, total)

    return maximum

#diagonal matrix sum -leetcode 1572
class Solution(object):
    def diagonalSum(self, mat):

        n = len(mat)

        total = 0

        for i in range(n):

            total += mat[i][i]

            if i != n - i - 1:
                total += mat[i][n - i - 1]

        return total