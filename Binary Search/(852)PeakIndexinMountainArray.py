class Solution:
    def peakIndexInMountainArray(self, arr):
        # Initialize boundaries excluding the first and last elements
        # to ensure mid-1 and mid+1 are always valid indices
        st = 1
        end = len(arr) - 2
        
        while st <= end:
            mid = st + (end - st) // 2
            
            # Check if mid is the peak element
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            
            # If we are on the increasing slope, peak is to the right
            if arr[mid - 1] < arr[mid]:
                st = mid + 1
            # If we are on the decreasing slope, peak is to the left
            else:
                end = mid - 1
                
        return -1
