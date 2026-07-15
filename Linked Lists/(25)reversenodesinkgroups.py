class Solution(object):
    def reverseKGroup(self, head, k):

        if head is None:
            return head

        # Step 1: Check if at least k nodes exist
        temp = head
        count = 0

        while temp and count < k:
            temp = temp.next
            count += 1

        # Less than k nodes left
        if count < k:
            return head

        # Step 2: Reverse remaining list
        nextHead = self.reverseKGroup(temp, k)

        # Step 3: Reverse current k nodes
        prev = nextHead
        curr = head
        count = 0

        while count < k:

            nextNode = curr.next

            curr.next = prev

            prev = curr

            curr = nextNode

            count += 1

        # Step 4: Return new head
        return prev