def previousSmaller(nums):

    stack = []
    ans = []

    for num in nums:

        while stack and stack[-1] >= num:
            stack.pop()

        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)

        stack.append(num)

    return ans