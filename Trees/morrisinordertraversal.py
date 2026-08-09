class Solution:

    def inorderTraversal(self, root):

        result = []
        current = root

        while current:

            # Case 1: No left subtree
            if current.left is None:

                result.append(current.val)
                current = current.right

            else:

                # Find inorder predecessor
                predecessor = current.left

                while (
                    predecessor.right is not None
                    and predecessor.right != current
                ):
                    predecessor = predecessor.right

                # First visit: create thread
                if predecessor.right is None:

                    predecessor.right = current
                    current = current.left

                # Second visit: remove thread
                else:

                    predecessor.right = None
                    result.append(current.val)
                    current = current.right

        return result