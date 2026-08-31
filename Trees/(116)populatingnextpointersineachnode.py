from collections import deque

class Solution:

    def connect(self, root):

        if root is None:
            return None

        queue = deque()
        queue.append(root)
        queue.append(None)

        previous = None

        while queue:

            current = queue.popleft()

            # End of current level
            if current is None:

                previous = None

                if queue:
                    queue.append(None)

                continue

            # Connect previous node to current node
            if previous is not None:
                previous.next = current

            previous = current

            # Add children
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return root
    
    
    
    
#recursive approach
class Solution:

    def connect(self, root):

        if root is None:
            return None

        leftmost = root

        while leftmost.left:

            head = leftmost

            while head:

                # Connect nodes with same parent
                head.left.next = head.right

                # Connect nodes across parents
                if head.next:
                    head.right.next = head.next.left

                head = head.next

            leftmost = leftmost.left

        return root    