
from torch import Node

class Solution(object):
    def removeElements(self, head, val):

        dummy = Node(0)
        dummy.next = head

        temp = dummy

        while temp.next:

            if temp.next.val == val:
                temp.next = temp.next.next

            else:
                temp = temp.next

        return dummy.next