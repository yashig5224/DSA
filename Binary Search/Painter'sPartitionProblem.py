class Solution:

    def isPossible(self, boards, n, k, maxTime):
        painters = 1
        time = 0

        for i in range(n):

            # A single board itself exceeds the allowed time
            if boards[i] > maxTime:
                return False

            # Assign board to current painter
            if time + boards[i] <= maxTime:
                time += boards[i]
            else:
                # Assign to next painter
                painters += 1
                time = boards[i]

                # More painters needed than available
                if painters > k:
                    return False

        return True

    def paintersPartition(self, boards, k):
        n = len(boards)

        # Impossible case
        if k > n:
            return -1

        low = max(boards)
        high = sum(boards)
        answer = -1

        while low <= high:

            mid = low + (high - low) // 2

            if self.isPossible(boards, n, k, mid):
                answer = mid
                high = mid - 1      # Try smaller maximum time
            else:
                low = mid + 1       # Increase allowed time

        return answer


# ---------------- Example ----------------

boards = [10, 20, 30, 40]
painters = 2

obj = Solution()
print(obj.paintersPartition(boards, painters))