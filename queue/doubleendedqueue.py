from collections import deque

dq = deque()

# Add from both ends
dq.append(10)       # back
dq.appendleft(20)   # front

# Remove from both ends
dq.pop()            # removes from back
dq.popleft()        # removes from front