class Solution:
    def celebrity(self, mat):
        n = len(mat)
        stack = list(range(n))

        # Eliminate impossible candidates
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()

            if mat[a][b] == 1:
                # a knows b -> a cannot be celebrity
                stack.append(b)
            else:
                # a doesn't know b -> b cannot be celebrity
                stack.append(a)

        candidate = stack.pop()

        # Verify candidate
        for i in range(n):
            if i != candidate:
                # Celebrity knows nobody
                if mat[candidate][i] == 1:
                    return -1

                # Everybody knows celebrity
                if mat[i][candidate] == 0:
                    return -1

        return candidate