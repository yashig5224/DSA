from collections import deque


def top_view(root):

    if root is None:
        return []

    queue = deque()

    top = {}

    queue.append((root, 0))

    while queue:

        node, hd = queue.popleft()

        if hd not in top:
            top[hd] = node.data

        if node.left:
            queue.append((node.left, hd - 1))

        if node.right:
            queue.append((node.right, hd + 1))

    answer = []

    for hd in sorted(top.keys()):
        answer.append(top[hd])

    return answer


#lc 102
from collections import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        ans = []
        queue = deque([root])

        while queue:

            level_size = len(queue)
            current_level = []

            for _ in range(level_size):

                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            ans.append(current_level)

        return ans