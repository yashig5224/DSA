class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        mp = {}

        # Find Next Greater Element for nums2
        for i in range(len(nums2) - 1, -1, -1):

            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                mp[nums2[i]] = stack[-1]
            else:
                mp[nums2[i]] = -1

            stack.append(nums2[i])

        ans = []

        # Get answers for nums1
        for num in nums1:
            ans.append(mp[num])

        return ans