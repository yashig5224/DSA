#leetcode 1 and 167 problems
# brute force approach 1
class Solution: 
    
    def twoSum(self, nums, target):

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):

                if nums[i] + nums[j] == target:
                    return [i, j]

# Example usage:
arr = [2, 7, 11, 15]
target = 9
print(f"brute force approach: {Solution().twoSum(arr, target)}")  # Output: [0, 1]



#optimal approach 167
class Solution:

    def twoSum(self, numbers, target):
        left = 0   # start pointer
        right = len(numbers) - 1  #end pointer 

        while left < right:
            current_sum = numbers[left] + numbers[right]   #calculate psum 

            if current_sum == target:
                return [left + 1, right + 1]  # ans(i,j)
            elif current_sum < target: 
                left += 1   #push start pointer forward to increase sum
            else:
                right -= 1  #push end pointer backward to decrease sum

        return []
    arr = [2, 7, 11, 15]
target = 9
print(f"optimal approach: {Solution().twoSum(arr, target)}")  # Output: [1, 2]

#using hashing
class Solution:
    def twoSum(self, nums, target):

        hashmap = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i






