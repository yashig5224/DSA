#BRUTE FORCE APPROACH
class Solution(object):
    def productExceptSelf(self, nums):
        
        n = len(nums)
        # Initialize an answer list filled with 1s of size n
        ans = [1] * n
        
        # Nested loops: For each element i, multiply all other elements j
        for i in range(n):
            for j in range(n):
                if i != j:
                    ans[i] *= nums[j]
                    
        return ans

#OPTIMAL APPROACH
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # 1. Answer array ko 1 se initialize kiya
        answer = [1] * n
        
        # Step 1: Store Prefix directly in the Answer array
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]
            
        # Step 2: Multiply Suffix on the fly using a single variable
        suffix = 1
        for i in range(n - 1, -1, -1):  # Loop runs from n-1 down to 0
            answer[i] *= suffix
            suffix *= nums[i]
            
        return answer
