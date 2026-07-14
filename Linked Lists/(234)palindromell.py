class Solution(object):
    def isPalindrome(self, head):

        if head is None or head.next is None:
            return True

        # Step 1 : Find Middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2 : Reverse Second Half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3 : Compare
        first = head
        second = prev

        while second:

            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True