#approach 1
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val):

        if not self.stack:
            self.stack.append((val, val))
        else:
            currMin = min(val, self.stack[-1][1])
            self.stack.append((val, currMin))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
#approach 2
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None

    def push(self, val):

        if not self.stack:
            self.stack.append(val)
            self.minimum = val

        elif val >= self.minimum:
            self.stack.append(val)

        else:
            self.stack.append(2 * val - self.minimum)
            self.minimum = val

    def pop(self):

        top = self.stack.pop()

        if top < self.minimum:
            self.minimum = 2 * self.minimum - top

    def top(self):

        top = self.stack[-1]

        if top >= self.minimum:
            return top
        else:
            return self.minimum

    def getMin(self):
        return self.minimum