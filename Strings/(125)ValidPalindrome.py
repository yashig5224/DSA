class Solution:
    def isPalindrome(self, s):

        left = 0         #str
        right = len(s) - 1      #end 

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1                        #if left is not alphanumeric, move left pointer to the right

            while left < right and not s[right].isalnum():
                right -= 1               #if right is not alphanumeric, move right pointer to the left

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True