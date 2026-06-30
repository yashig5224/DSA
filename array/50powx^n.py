class Solution(object):
    def myPow(self, x, n):
        # 1. Quick Base Cases
        if n == 0:
            return 1
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x == -1:
            return 1 if n % 2 == 0 else -1
            
        # 2. Handle Negative Power
        if n < 0:
            x = 1 / x
            n = -n

        # 3. Fast Power Logic
        ans = 1
        while n:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2

        return ans
