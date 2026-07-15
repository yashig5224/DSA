"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):

        if not head:
            return head

        def dfs(node):

            curr = node
            last = None

            while curr:

                nextNode = curr.next

                if curr.child:

                    childHead = curr.child
                    childTail = dfs(childHead)

                    curr.next = childHead
                    childHead.prev = curr
                    curr.child = None

                    if nextNode:
                        childTail.next = nextNode
                        nextNode.prev = childTail

                    last = childTail

                else:
                    last = curr

                curr = nextNode

            return last

        dfs(head)

        return head