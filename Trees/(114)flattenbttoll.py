class Solution:

    def flatten(self, root):

        self.last = None

        def reverse_preorder(node):

            if node is None:
                return

            # Right
            reverse_preorder(node.right)

            # Left
            reverse_preorder(node.left)

            # Root
            node.right = self.last
            node.left = None

            self.last = node

        reverse_preorder(root)
        
        
#iterative approach to reduce sc
class Solution:

    def flatten(self, root):

        current = root

        while current:

            if current.left:

                predecessor = current.left

                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = current.right

                current.right = current.left
                current.left = None

            current = current.right        