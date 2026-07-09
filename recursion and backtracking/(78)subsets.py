class Solution(object):
    def subsets(self, nums):
        ans = []

        def backtrack(index, subset):
            if index == len(nums):
                ans.append(subset[:])   # Copy current subset
                return

            # Include current element
            subset.append(nums[index])
            backtrack(index + 1, subset)

            # Backtrack
            subset.pop()

            # Exclude current element
            backtrack(index + 1, subset)

        backtrack(0, [])
        return ans