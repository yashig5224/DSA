class Solution:
    def isPossible(self, books, n, m, maxPages):
        students = 1
        pages = 0

        for i in range(n):
            # A single book exceeds the allowed limit
            if books[i] > maxPages:
                return False

            # Allocate book to current student
            if pages + books[i] <= maxPages:
                pages += books[i]
            else:
                # Allocate to next student
                students += 1
                pages = books[i]

                # More students needed than available
                if students > m:
                    return False

        return True

    def bookAllocation(self, books, m):
        n = len(books)

        # Impossible case
        if m > n:
            return -1

        low = max(books)
        high = sum(books)
        answer = -1

        while low <= high:
            mid = low + (high - low) // 2

            if self.isPossible(books, n, m, mid):
                answer = mid
                high = mid - 1      # Try smaller answer
            else:
                low = mid + 1       # Need larger answer

        return answer


# Example
books = [10, 20, 30, 40]
students = 2

obj = Solution()
print(obj.bookAllocation(books, students))