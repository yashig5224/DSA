class Solution(object):
    def swapPairs(self, head):

        # Base Case
        if head is None or head.next is None:
            return head

        prev = None
        first = head
        second = head.next

        # New head after first swap
        head = second

        while first and second:

            third = second.next

            # Swap
            second.next = first
            first.next = third

            # Connect previous pair
            if prev:
                prev.next = second

            # Move pointers
            prev = first
            first = third

            if third:
                second = third.next
            else:
                second = None

        return head