#approach 1: brute force
#using nums.sort() function

#approach 2:using two passes
class Solution:
    def sortColors(self, nums):

        zero = 0
        one = 0
        two = 0

        for num in nums:
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1
            else:
                two += 1

        index = 0

        while zero:
            nums[index] = 0
            zero -= 1
            index += 1

        while one:
            nums[index] = 1
            one -= 1
            index += 1

        while two:
            nums[index] = 2
            two -= 1
            index += 1
            
            
#approach 3:Dutch National Flag Algorithm (Best)
            
        
    