class Solution:
    def findMissingAndRepeatedValues(self, grid):

        n = len(grid)

        seen = set()

        duplicate = 0
        actual_sum = 0

        for row in grid:
            for num in row:

                actual_sum += num

                if num in seen:
                    duplicate = num

                else:
                    seen.add(num)

        total = n * n
        expected_sum = total * (total + 1) // 2

        missing = duplicate + expected_sum - actual_sum

        return [duplicate, missing]