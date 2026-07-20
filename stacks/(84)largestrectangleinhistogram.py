class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)

        left = [-1] * n
        right = [n] * n

        stack = []

        # Left Smaller
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1]

            stack.append(i)

        stack = []

        # Right Smaller
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]

            stack.append(i)

        ans = 0

        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            ans = max(ans, area)

        return ans