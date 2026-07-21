class StockSpanner(object):

    def __init__(self):
        self.prices = []
        self.stack = []

    def next(self, price):
        self.prices.append(price)

        i = len(self.prices) - 1

        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()

        if not self.stack:
            span = i + 1
        else:
            span = i - self.stack[-1]

        self.stack.append(i)

        return span