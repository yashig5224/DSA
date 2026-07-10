class Solution(object):

    def partition(self, s):

        ans = []
        current = []

        def isPalindrome(left, right):

            while left < right:

                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        def solve(index):

            if index == len(s):
                ans.append(current[:])
                return

            for end in range(index, len(s)):

                if isPalindrome(index, end):

                    current.append(s[index:end + 1])

                    solve(end + 1)

                    current.pop()

        solve(0)

        return ans