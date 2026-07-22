from collections import deque

class Solution(object):

    def firstUniqChar(self, s):

        freq = {}
        q = deque()

        for i in range(len(s)):

            ch = s[i]

            # Increase frequency
            freq[ch] = freq.get(ch, 0) + 1

            # Add index to queue
            q.append(i)

            # Remove repeated characters
            while q and freq[s[q[0]]] > 1:
                q.popleft()

        if not q:
            return -1

        return q[0]