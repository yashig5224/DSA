from collections import deque

class Queue:

    def __init__(self):
        self.q = deque()

    # Push / Enqueue
    def push(self, val):
        self.q.append(val)

    # Pop / Dequeue
    def pop(self):
        if self.empty():
            print("Queue is empty")
            return

        return self.q.popleft()

    # Front
    def front(self):
        if self.empty():
            print("Queue is empty")
            return

        return self.q[0]

    # Empty
    def empty(self):
        return len(self.q) == 0


q = Queue()

q.push(10)
q.push(20)
q.push(30)

print(q.front())  # 10

print(q.pop())    # 10
print(q.pop())    # 20

print(q.empty())  # False