
from torch import Node


class Solution(object):
    def copyRandomList(self, head):

        if not head:
            return None

        oldToNew = {}

        curr = head

        newHead = Node(curr.val)
        oldToNew[curr] = newHead

        oldCurr = curr.next
        newCurr = newHead

        while oldCurr:

            copy = Node(oldCurr.val)

            newCurr.next = copy

            newCurr = copy

            oldToNew[oldCurr] = copy

            oldCurr = oldCurr.next

        oldCurr = head
        newCurr = newHead

        while oldCurr:

            if oldCurr.random:
                newCurr.random = oldToNew[oldCurr.random]

            oldCurr = oldCurr.next
            newCurr = newCurr.next

        return newHead