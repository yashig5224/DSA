class Solution(object):
    def sortedArrayToBST(self, nums):
        def helper(start, end):
            # Base case
            if start > end:
                return None

            # Find middle element
            mid = start + (end - start) // 2

            # Create root
            root = TreeNode(nums[mid])

            # Build left subtree
            root.left = helper(start, mid - 1)

            # Build right subtree
            root.right = helper(mid + 1, end)

            return root

        return helper(0, len(nums) - 1)
        