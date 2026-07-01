class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)
        
        # Base case: if array has only one element
        if n == 1:
            return nums[0]
            
        st = 0
        end = n - 1
        
        while st <= end:
            mid = st + (end - st) // 2
            
            # ① Check if mid is the first element and is unique
            if mid == 0 and nums[0] != nums[1]:
                return nums[mid]
                
            # ② Check if mid is the last element and is unique
            if mid == n - 1 and nums[n - 1] != nums[n - 2]:
                return nums[mid]
                
            # Check if mid itself is the single unique element
            if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]
                
            # If mid index is even
            if mid % 2 == 0:
                # If duplicate is on the left, right side is disrupted; go left
                if nums[mid - 1] == nums[mid]:
                    end = mid - 1
                # Otherwise, left side is fine; go right
                else:
                    st = mid + 1
                    
            # If mid index is odd
            else:
                # If duplicate is on the left, left side is fine; go right
                if nums[mid - 1] == nums[mid]:
                    st = mid + 1
                # Otherwise, right side is fine; go left
                else:
                    end = mid - 1
                    
        return -1
