#APPROACH 1:BRUTE FORCE  (RESULTS IN TLE)
class Solution:
    def threeSum(self, nums):

        ans = set()
        n = len(nums)

        for i in range(n):

            for j in range(i + 1, n):

                for k in range(j + 1, n):

                    if nums[i] + nums[j] + nums[k] == 0:

                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))

                        ans.add(triplet)

        return list(ans)
    
#APPROACH 2:HASH SET    
class Solution:
    def threeSum(self, nums):

        nums.sort()

        ans = set()

        n = len(nums)

        for i in range(n):

            seen = set()

            for j in range(i + 1, n):

                third = -(nums[i] + nums[j])

                if third in seen:

                    ans.add((nums[i], third, nums[j]))

                seen.add(nums[j])

        return list(ans)
    
#APPROACH 3:TWO POINTERS
class Solution:
    def threeSum(self, nums):

        nums.sort()

        ans = []

        n = len(nums)

        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:

                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return ans  