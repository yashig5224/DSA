def removeCycle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    if fast is None or fast.next is None:
        return

    slow = head
    prev = None

    while slow != fast:

        prev = fast
        slow = slow.next
        fast = fast.next

    prev.next = None