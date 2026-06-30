#BRUTE FORCE APPROACH :TLE 
class Solution(object):
    def maxArea(self, height):
        max_water = 0
        
        # Nested loops checking every single pair
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                w = j - i
                ht = min(height[i], height[j])
                curr_water = w * ht
                
                max_water = max(max_water, curr_water)
                
        return max_water


#OPTIMAL APPROACH : TWO POINTERS
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        lp = 0
        rp = len(height) - 1

        while lp < rp:
            w = rp - lp
            ht = min(height[lp], height[rp])
            curr_water = w * ht
            max_water = max(max_water, curr_water)

            # Python equivalent of the C++ ternary operator syntax
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1

        return max_water
