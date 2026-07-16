class Solution(object):
    def isValid(self, s):

        stack = []

        for ch in s:

            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            else:

                if not stack:
                    return False

                top = stack[-1]

                if (top == '(' and ch == ')') or \
                   (top == '{' and ch == '}') or \
                   (top == '[' and ch == ']'):

                    stack.pop()

                else:
                    return False

        return len(stack) == 0