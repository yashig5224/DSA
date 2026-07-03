class Solution:

    def checkInclusion(self, s1, s2):

        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        windowCount = [0] * 26

        # Count frequency of s1
        for ch in s1:
            s1Count[ord(ch) - ord('a')] += 1

        windowSize = len(s1)

        # First window
        for i in range(windowSize):
            windowCount[ord(s2[i]) - ord('a')] += 1

        if s1Count == windowCount:
            return True

        # Slide the window
        for i in range(windowSize, len(s2)):

            # Add new character
            windowCount[ord(s2[i]) - ord('a')] += 1

            # Remove old character
            windowCount[ord(s2[i - windowSize]) - ord('a')] -= 1

            if s1Count == windowCount:
                return True

        return False