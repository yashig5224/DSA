class Solution:

    def binaryTreePaths(self, root):

        answer = []

        def dfs(node, path):

            if node is None:
                return

            # Add current node to path
            if path:
                path += "->" + str(node.val)
            else:
                path = str(node.val)

            # Leaf node
            if node.left is None and node.right is None:
                answer.append(path)
                return

            # Explore left and right
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")

        return answer
    
    
#backtracking version
class Solution:

    def binaryTreePaths(self, root):

        answer = []
        path = []

        def dfs(node):

            if node is None:
                return

            path.append(str(node.val))

            # Leaf node
            if node.left is None and node.right is None:
                answer.append("->".join(path))

            else:
                dfs(node.left)
                dfs(node.right)

            # Backtrack
            path.pop()

        dfs(root)

        return answer