# leetcode 169

#brute force approach
def majority_element_brute_force(nums):
    n = len(nums)   # calculate the length of the array
    threshold = n // 2  # calculate threshold 

    # Outer loop selects an element to check
    for i in range(n):
        current_element = nums[i]          #pick no to check 
        count = 0

        # Inner loop counts the occurrences of current_element
        for j in range(n):
            if nums[j] == current_element:   #counts every time in the list to check the occurence and then add+1
                count += 1

        # Check if the count exceeds the majority threshold
        if count > threshold:
            return current_element  #check the condition and return if element exceeds thresshold

    return -1  # Fallback if no majority element exists


# Example usage:
nums = [2, 2, 1, 1, 1, 2, 2]
print(f"Majority element (brute force): {majority_element_brute_force(nums)}")  # Output: 2



#Sorting approach
def majority_element_sorting(nums):
    # Step 1: Sort the array in ascending order
    nums.sort()

    # Step 2: The middle element is always the majority element
    middle_index = len(nums) // 2
    return nums[middle_index]


# Example usage:
nums = [2, 2, 1, 1, 1, 2, 2]
print(f"Majority element (sorting): {majority_element_sorting(nums)}")  # Output: 2



#Moore's Voting Algorithm
class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
# Example usage:
nums = [2, 2, 1, 1, 1, 2, 2]
print(f"Majority element (Moore's Voting Algorithm): {Solution().majorityElement(nums)}")  # Output: 2

