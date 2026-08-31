class Solution:

    def recoverTree(self, root):

        self.prev = None
        self.first = None
        self.second = None

        def inorder(node):

            if node is None:
                return

            # Left subtree
            inorder(node.left)

            # Check violation
            if self.prev and self.prev.val > node.val:

                if self.first is None:
                    self.first = self.prev

                self.second = node

            # Update previous
            self.prev = node

            # Right subtree
            inorder(node.right)

        inorder(root)

        # Swap the values
        self.first.val, self.second.val = \
            self.second.val, self.first.val
            
            
            
#morris inorder traversal
class Solution:

    def recoverTree(self, root):

        first = None
        second = None
        prev = None

        current = root

        while current:

            if current.left is None:

                # Process current
                if prev and prev.val > current.val:

                    if first is None:
                        first = prev

                    second = current

                prev = current

                current = current.right

            else:

                # Find inorder predecessor
                predecessor = current.left

                while (predecessor.right is not None and
                       predecessor.right != current):

                    predecessor = predecessor.right

                # Create thread
                if predecessor.right is None:

                    predecessor.right = current
                    current = current.left

                # Remove thread
                else:

                    predecessor.right = None

                    # Process current
                    if prev and prev.val > current.val:

                        if first is None:
                            first = prev

                        second = current

                    prev = current

                    current = current.right

        # Swap misplaced values
        first.val, second.val = second.val, first.val            