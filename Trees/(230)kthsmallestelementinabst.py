#recursive approach
class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.answer = -1

        def inorder(node):
            if node is None:
                return

            # Left
            inorder(node.left)

            # Root
            self.count += 1

            if self.count == k:
                self.answer = node.val
                return

            # Right
            inorder(node.right)

        inorder(root)

        return self.answer
    
    
#iterative approach
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        curr = root

        while True:

            # Go as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # Visit node
            curr = stack.pop()
            k -= 1

            # kth node found
            if k == 0:
                return curr.val

            # Move right
            curr = curr.right    