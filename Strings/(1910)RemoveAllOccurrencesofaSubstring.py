class Solution:
    def removeOccurrences(self, s, part):

        while part in s:
            index = s.find(part)
            s = s[:index] + s[index + len(part):]

        return s
    
##SHORTER VERSION
class Solution(object):
    def removeOccurrences(self, s, part):
        while part in s:
            s = s.replace(part, "", 1)
        return s
