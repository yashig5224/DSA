from collections import deque

def reverseFirstK(q, k):

    stack = []

    # Step 1: Put first k elements into stack
    for _ in range(k):
        stack.append(q.popleft())

    # Step 2: Put them back into queue
    while stack:
        q.append(stack.pop())

    # Step 3: Move remaining elements to the back
    remaining = len(q) - k

    for _ in range(remaining):
        q.append(q.popleft())

    return q