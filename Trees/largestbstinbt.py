class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Info:

    def __init__(self, minimum, maximum, size):
        self.minimum = minimum
        self.maximum = maximum
        self.size = size


class Solution:

    def largestBST(self, root):

        def solve(node):

            # Base case
            if node is None:
                return Info(
                    float('inf'),
                    float('-inf'),
                    0
                )

            # Get information from left subtree
            left = solve(node.left)

            # Get information from right subtree
            right = solve(node.right)

            # Check if current subtree is a BST
            if left.maximum < node.val < right.minimum:

                minimum = min(node.val, left.minimum)
                maximum = max(node.val, right.maximum)

                size = left.size + right.size + 1

                return Info(minimum, maximum, size)

            # Current subtree is NOT a BST
            return Info(
                float('-inf'),
                float('inf'),
                max(left.size, right.size)
            )

        return solve(root).size