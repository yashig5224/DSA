class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Reverse the entire string
        s = s[::-1]
        
        ans = ""
        n = len(s)
        i = 0
        
        # Step 2: Loop through to find and reverse individual words
        while i < n:
            # Skip spaces between words
            if s[i] == ' ':
                i += 1
                continue
                
            # Extract a single reversed word
            word = ""
            while i < n and s[i] != ' ':
                word += s[i]
                i += 1
            
            # Reverse the extracted word back to its correct order
            word = word[::-1]
            
            # Append it to the final result with a leading space
            if len(word) > 0:
                ans += " " + word
        
        # Remove the very first leading space
        return ans[1:] if ans else ""
