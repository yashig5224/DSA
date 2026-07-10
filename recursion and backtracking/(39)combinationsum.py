class Solution(object):

    def combinationSum(self, candidates, target):

        ans = []
        current = []

        def solve(index, target):

            if target == 0:
                ans.append(current[:])
                return

            if target < 0:
                return

            if index == len(candidates):
                return

            # Include current element
            current.append(candidates[index])

            solve(index, target - candidates[index])

            current.pop()

            # Exclude current element
            solve(index + 1, target)

        solve(0, target)

        return ans