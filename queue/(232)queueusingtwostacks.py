class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):

        # Move all elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # Add new element
        self.s1.append(x)

        # Move elements back
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):

        if not self.s1:
            return -1

        return self.s1.pop()

    def peek(self):

        if not self.s1:
            return -1

        return self.s1[-1]

    def empty(self):

        return len(self.s1) == 0