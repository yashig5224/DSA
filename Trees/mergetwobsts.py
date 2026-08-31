class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def mergeBSTs(self, root1, root2):

        # Step 1: Inorder traversals
        arr1 = []
        arr2 = []

        self.inorder(root1, arr1)
        self.inorder(root2, arr2)

        # Step 2: Merge sorted arrays
        merged = self.merge(arr1, arr2)

        # Step 3: Build balanced BST
        return self.buildBST(merged, 0, len(merged) - 1)

    def inorder(self, root, arr):

        if root is None:
            return

        self.inorder(root.left, arr)

        arr.append(root.val)

        self.inorder(root.right, arr)

    def merge(self, arr1, arr2):

        i = 0
        j = 0
        result = []

        while i < len(arr1) and j < len(arr2):

            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1

            else:
                result.append(arr2[j])
                j += 1

        while i < len(arr1):
            result.append(arr1[i])
            i += 1

        while j < len(arr2):
            result.append(arr2[j])
            j += 1

        return result

    def buildBST(self, arr, left, right):

        if left > right:
            return None

        mid = (left + right) // 2

        root = TreeNode(arr[mid])

        root.left = self.buildBST(arr, left, mid - 1)

        root.right = self.buildBST(arr, mid + 1, right)

        return root