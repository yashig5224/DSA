from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):

        if root is None:
            return 0

        queue = deque([(root, 0)])

        maximum_width = 0

        while queue:

            level_size = len(queue)

            _, first = queue[0]

            for i in range(level_size):

                node, index = queue.popleft()

                # Normalize index
                index -= first

                if i == 0:
                    left = index

                if i == level_size - 1:
                    right = index

                if node.left:
                    queue.append((node.left, 2 * index + 1))

                if node.right:
                    queue.append((node.right, 2 * index + 2))

            maximum_width = max(maximum_width, right - left + 1)

        return maximum_width