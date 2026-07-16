def stockSpan(price):

    n = len(price)
    span = [0] * n
    stack = []

    for i in range(n):

        while stack and price[stack[-1]] <= price[i]:
            stack.pop()

        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]

        stack.append(i)

    return span