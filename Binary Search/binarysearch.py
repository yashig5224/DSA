#Iterative method
def binary_search(arr, target):
    # Initialize start (st) and end pointers
    st = 0
    end = len(arr) - 1
    
    # Loop until the pointers cross
    while st <= end:
        # 1. Find the mid index
        mid = st + (end - st) // 2 #this formula does not cause overflow
        
        # 2. If target is greater, look in the right half
        if target > arr[mid]:
            st = mid + 1   #2nd half
            
        # 3. If target is smaller, look in the left half
        elif target < arr[mid]:
            end = mid - 1   #1st half
            
        # 4. Target found, return index
        else:
            return mid
            
    # Return -1 if target is not present in the array
    return -1

# Example usage from the image:
arr = [-1, 0, 3, 4, 5, 9, 12]
target = 12 

result = binary_search(arr, target)
print(f"Target found at index: {result}")  # Output: 6


#Recursive method

class Solution:
    def search(self, nums, target):

        def solve(start, end):
            if start > end:
                return -1

            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                return solve(mid + 1, end)

            else:
                return solve(start, mid - 1)

        return solve(0, len(nums) - 1)

# Example usage from the image:
arr = [-1, 0, 3, 5, 9, 12]
tar = 0
st = 0
end = len(arr) - 1

result = binary_search_recursive(arr, tar, st, end)
print(f"Target found at index: {result}")  # Output: 1
