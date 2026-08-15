#recursive approach 
class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if root is None:
            return None

        # Both nodes are on the left
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Both nodes are on the right
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Nodes split OR root is p/q
        return root

#iterative approach
class Solution:
    def lowestCommonAncestor(self, root, p, q):

        while root:

            if p.val < root.val and q.val < root.val:
                root = root.left

            elif p.val > root.val and q.val > root.val:
                root = root.right

            else:
                return root