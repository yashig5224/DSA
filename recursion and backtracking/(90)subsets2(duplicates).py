class Solution:

    def solve(self, nums, index, subset, ans):

        ans.append(subset[:])

        for i in range(index, len(nums)):

            if i > index and nums[i] == nums[i-1]:
                continue

            subset.append(nums[i])

            self.solve(nums, i + 1, subset, ans)

            subset.pop()

    def subsetsWithDup(self, nums):

        nums.sort()

        ans = []

        self.solve(nums, 0, [], ans)

        return ans