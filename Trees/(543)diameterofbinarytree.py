#brute force approach
from Trees.binarytreerecursion import height


def diameter(root):

    if root is None:
        return 0

    left_diameter = diameter(root.left)

    right_diameter = diameter(root.right)

    current = height(root.left) + height(root.right)

    return max(current, left_diameter, right_diameter)

#optimized approach
class Solution:

    def diameterOfBinaryTree(self, root):

        self.diameter = 0

        def height(node):

            if node is None:
                return 0

            left = height(node.left)

            right = height(node.right)

            self.diameter = max(
                self.diameter,
                left + right
            )

            return 1 + max(left, right)

        height(root)

        return self.diameter