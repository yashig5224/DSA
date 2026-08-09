
#brute force
class Solution:

    def buildTree(self, preorder, inorder):

        self.preorderIndex = 0

        def build(left, right):

            if left > right:
                return None

            root_value = preorder[self.preorderIndex]
            self.preorderIndex += 1

            root = TreeNode(root_value)

            inorder_index = inorder.index(root_value)

            root.left = build(left, inorder_index - 1)

            root.right = build(inorder_index + 1, right)

            return root

        return build(0, len(inorder) - 1)



#optimized 
class Solution:

    def buildTree(self, preorder, inorder):

        inorder_map = {}

        for i, value in enumerate(inorder):
            inorder_map[value] = i

        self.preorderIndex = 0

        def build(left, right):

            if left > right:
                return None

            root_value = preorder[self.preorderIndex]
            self.preorderIndex += 1

            root = TreeNode(root_value)

            inorder_index = inorder_map[root_value]

            root.left = build(left, inorder_index - 1)

            root.right = build(inorder_index + 1, right)

            return root

        return build(0, len(inorder) - 1)