class Solution:
    def nextPermutation(self, nums):

        n = len(nums)

        pivot = -1

        # Step 1: Find pivot
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # Step 2: If no pivot, reverse whole array
        if pivot == -1:
            nums.reverse()
            return

        # Step 3: Find successor
        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        # Step 4: Reverse suffix
        left = pivot + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1