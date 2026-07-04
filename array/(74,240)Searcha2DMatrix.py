# 74-binary search in 2d matrix
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
    
#74 treat matrix as a 1d array and apply binary search
class Solution:
    def searchMatrix(self, matrix, target):

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:

            mid = (left + right) // 2

            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
    
    
#240 search a 2d matrix II
class Solution:
    def searchMatrix(self, matrix, target):

        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1

        while row < rows and col >= 0:

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                col -= 1

            else:
                row += 1

        return False        