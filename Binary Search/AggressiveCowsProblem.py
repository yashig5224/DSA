class Solution:

    # Check if it is possible to place all cows
    # with at least minDistance between them
    def isPossible(self, stalls, n, cows, minDistance):

        cowsPlaced = 1                 # Place first cow in first stall
        lastPosition = stalls[0]

        for i in range(1, n):

            if stalls[i] - lastPosition >= minDistance:
                cowsPlaced += 1
                lastPosition = stalls[i]

                # All cows placed successfully
                if cowsPlaced == cows:
                    return True

        return False

    def aggressiveCows(self, stalls, cows):

        stalls.sort()                  # Step 1: Sort the stalls

        n = len(stalls)

        low = 1
        high = stalls[n - 1] - stalls[0]

        answer = -1

        while low <= high:

            mid = low + (high - low) // 2

            if self.isPossible(stalls, n, cows, mid):
                answer = mid
                low = mid + 1          # Try a larger minimum distance
            else:
                high = mid - 1         # Reduce the minimum distance

        return answer


# ---------------- Example ----------------

stalls = [1, 2, 4, 8, 9]
cows = 3

obj = Solution()
print(obj.aggressiveCows(stalls, cows))