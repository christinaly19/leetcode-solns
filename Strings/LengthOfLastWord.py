# 58: Length of Last Word (Easy)
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastLetterIndex = 0
        count = 0
        for i in range(len(s)):
            if s[i] != " ":
                lastLetterIndex = i

        while (lastLetterIndex >= 0 and s[lastLetterIndex] != " ") :
            count = count + 1
            lastLetterIndex = lastLetterIndex - 1
        
        return count
