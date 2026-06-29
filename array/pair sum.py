#leetcode 1 and 167 problems
# brute force approach
def pair_sum_brute_force(arr, target):
    n = len(arr)
    
    # Outer loop selects the first element
    for i in range(n):
        # Inner loop selects the second element (always ahead of i to avoid pairing with itself)
        for j in range(i + 1, n):
            # Check if the sum of the pair matches the target
            if arr[i] + arr[j] == target:
                return [arr[i], arr[j]]  # Returns the values. Use [i, j] if you need the indices.
                
    return []  # Return an empty list if no pair is found

# Example usage:
arr = [2, 7, 11, 15]
target = 9
print(f"brute force approach: {pair_sum_brute_force(arr, target)}")  # Output: [2, 7]



#optimal approach
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
