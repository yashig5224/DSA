class Solution:
    def search(self, nums, target):
        st = 0
        end = len(nums) - 1
        
        while st <= end:
            mid = st + (end - st) // 2
            
            # If target is found at mid
            if nums[mid] == target:
                return mid
            
            # Check if Left half is sorted
            if nums[st] <= nums[mid]:
                # Check if target lies within the sorted left half
                if nums[st] <= target and target <= nums[mid]:
                    end = mid - 1  # Go left
                else:
                    st = mid + 1   # Go right
                    
            # Otherwise, Right half must be sorted
            else:
                # Check if target lies within the sorted right half
                if nums[mid] <= target and target <= nums[end]:
                    st = mid + 1   # Go right
                else:
                    end = mid - 1  # Go left
                    
        return -1
